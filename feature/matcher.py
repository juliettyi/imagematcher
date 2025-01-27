# this syntax allow matcher.py to be imported from
# both current dir like: from matcher import Matcher
# and upper dir like: from feature.matcher import Matcher
if __package__:
  from .constants import *
  from .feature import FeatureGen
else:
  from constants import *
  from feature import FeatureGen
  
from scipy.sparse import csr_matrix
from scipy.sparse import load_npz

import json
import numpy
import os


class Matcher(object):
  '''Match feature.'''
  def __init__(self, feature_dir):
    self._feature_dir = feature_dir
    with open(os.path.join(feature_dir, ID_TO_FN)) as f:
      self._id_to_fn = json.load(f)
    with open(os.path.join(feature_dir, FN_TO_ID)) as f:
      self._fn_to_id = json.load(f)
    # self._features = numpy.load(os.path.join(feature_dir, FEATURE_FN))
    self._features = load_npz(os.path.join(feature_dir, FEATURE_FN))
    self._fg = FeatureGen()

  def match(self, feature, top_n=5):
    # r = numpy.matmul(self._features, feature)
    r = self._features.dot(feature)
    print(r.shape)
    r = r.reshape([-1])
    ind = numpy.argpartition(r, -top_n)[-top_n:]
    top = {}
    for i in ind:
      print('{}, score: {}'.format(self._id_to_fn[str(i)], r[i]))
      top[self._id_to_fn[str(i)]] = r[i]
    return top

  def match_file(self, fn, top_n=5):
    feature = self._fg.gen_feature(fn)
    return self.match(feature, top_n=top_n)
