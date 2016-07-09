#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from .estimator_base import H2OEstimator


class H2OAggregatorEstimator(H2OEstimator):
    """
    Aggregator
    ----------

    Parameters (optional, unless specified otherwise)
    ----------
      model_id : str
        Destination id for this model; auto-generated if not specified.

      training_frame : str
        Id of the training data frame (Not required, to allow initial validation of model parameters).

      response_column : VecSpecifier
        Response variable column.

      ignored_columns : list(str)
        Names of columns to ignore for training.

      ignore_const_cols : bool
        Ignore constant columns.
        Default: True

      radius_scale : float
        Radius scaling
        Default: 1.0

      transform : "NONE" | "STANDARDIZE" | "NORMALIZE" | "DEMEAN" | "DESCALE"
        Transformation of training data
        Default: "NORMALIZE"

      categorical_encoding : "AUTO" | "Enum" | "OneHotInternal" | "OneHotExplicit" | "Binary" | "Eigen"
        Encoding scheme for categorical features
        Default: "AUTO"

    """
    def __init__(self, **kwargs):
        super(H2OAggregatorEstimator, self).__init__()
        self._parms = {}
        for name in ["model_id", "training_frame", "response_column", "ignored_columns", "ignore_const_cols",
                     "radius_scale", "transform", "categorical_encoding"]:
            pname = name[:-1] if name[-1] == '_' else name
            self._parms[pname] = kwargs[name] if name in kwargs else None

    @property
    def training_frame(self):
        return self._parms["training_frame"]

    @training_frame.setter
    def training_frame(self, value):
        self._parms["training_frame"] = value

    @property
    def response_column(self):
        return self._parms["response_column"]

    @response_column.setter
    def response_column(self, value):
        self._parms["response_column"] = value

    @property
    def ignored_columns(self):
        return self._parms["ignored_columns"]

    @ignored_columns.setter
    def ignored_columns(self, value):
        self._parms["ignored_columns"] = value

    @property
    def ignore_const_cols(self):
        return self._parms["ignore_const_cols"]

    @ignore_const_cols.setter
    def ignore_const_cols(self, value):
        self._parms["ignore_const_cols"] = value

    @property
    def radius_scale(self):
        return self._parms["radius_scale"]

    @radius_scale.setter
    def radius_scale(self, value):
        self._parms["radius_scale"] = value

    @property
    def transform(self):
        return self._parms["transform"]

    @transform.setter
    def transform(self, value):
        self._parms["transform"] = value

    @property
    def categorical_encoding(self):
        return self._parms["categorical_encoding"]

    @categorical_encoding.setter
    def categorical_encoding(self, value):
        self._parms["categorical_encoding"] = value

