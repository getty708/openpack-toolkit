"""Activity Set in Open Pack

* Work-process level annotation

"""
from dataclasses import dataclass
from logging import getLogger
from typing import Tuple, Union

import numpy as np

logger = getLogger(__name__)


@dataclass
class ActClass():
    id: int
    name: str
    is_ignore: bool = False


@dataclass
class ActSet():
    classes: Tuple[ActClass, ...]

    def __len__(self) -> int:
        return len(self.classes)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current == len(self.classes):
            raise StopIteration
        cls = self.classes[self._current]
        self._current += 1
        return cls

    def to_tuple(
        self, keep_actclass: bool = False,
    ) -> Union[Tuple[Tuple[int, str], ...], Tuple[ActClass, ...]]:
        """Returns a activity classes as a tuple.

        Args:
            keep_actclass (bool, optional): If True, return a tuple of ActClass.
                Otherwise, return a pure tuple, i.e., ``Tuple[Tuple[id:int, name:str], ...]``.
                Defaults to False.

        Returns:
            Union[Tuple[Tuple[int, str], ...], Tuple[ActClass, ...]]
        """
        if keep_actclass:
            return self.classes

        classes = [(cls.id, cls.name) for cls in self.classes]
        return tuple(classes)

    def get_ids(self) -> Tuple[int]:
        """Returns a tuple of class IDs.

        Returns:
            Tuple[int]
        """
        return tuple([act.id for act in self.classes])

    def get_ignore_class_index(self) -> Union[int, Tuple]:
        """Return the index of ignore classes, i.e., ``is_ignore=True``.
        If there are only one ignore class, return the index as int.

        Returns:
            Union[int, Tuple]
        """
        index = tuple([i for i, act in enumerate(
            self.classes) if act.is_ignore])
        if len(index) == 1:
            return index[0]
        return index

    def get_ignore_class_id(self) -> Union[int, Tuple]:
        """Return the ID of ignore classes, i.e., ``is_ignore=True``.
        If there are only one ignore class, return the ID as int.

        Returns:
            Union[int, Tuple]
        """
        ids = tuple([act.id for act in self.classes if act.is_ignore])
        if len(ids) == 1:
            return ids[0]
        return ids

    def convert_id_to_index(self, ids: np.ndarray) -> np.ndarray:
        """Translate activity ID into activity index.

        Args:
            ids (np.ndarray): 1d array of activity IDs.

        Returns:
            np.ndarray: 1d array of activity index.
        """
        assert ids.ndim == 1

        translator = {act.id: i for i, act in enumerate(self.classes)}
        logger.debug(f"convert activity IDs into index by {translator}.")
        assert set(ids) <= set(translator.keys()), (
            f"index have unexpected class ID. {set(ids) - set(translator.keys())}"
        )

        index = np.array([translator[val] for val in ids])
        return index.astype(np.int64)

    def convert_index_to_id(self, index: np.ndarray) -> np.ndarray:
        """Translate activity index into activity ID.

        Args:
            index (np.ndarray): 1d array of activity index.

        Returns:
            np.ndarray: 1d array of activity IDs.
        """
        assert index.ndim == 1

        translator = {i: act.id for i, act in enumerate(self.classes)}
        logger.debug(f"convert activity IDs into index by {translator}.")
        assert set(index) <= set(translator.keys()), (
            f"index have unexpected class ID. {set(index) - set(translator.keys())}"
        )

        ids = np.array([translator[val] for val in index])
        return ids.astype(np.int64)


""" Activity Set Definitions
"""

OPENPACK_WORKPROCESS_CLASSES = ActSet((
    ActClass(100, "Picking"),
    ActClass(200, "MoveItemLabel"),
    ActClass(300, "AssembleBox"),
    ActClass(400, "PackInBox"),
    ActClass(500, "CloseBox"),
    ActClass(600, "ReadLabel"),
    ActClass(700, "AttachLabel"),
    ActClass(800, "PutOnCartRack"),
    ActClass(900, "Pen"),
    ActClass(1000, "Null", is_ignore=True),
))
