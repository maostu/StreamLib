==========
StreamLib 
==========
-------------------------------------------
python library for streaming algorithms
-------------------------------------------

Document can be found in http://xmerge.me/StreamLib/.

Overview
-------------
Algorithms included:

* Sketch

  + Count Min Sketch [cm05]_ -- DONE
  + Count Median Sketch [cm05]_ -- DONE
  + Count Sketch [ccfc04]_ -- DONE
  + BJKST Sketch [bjkst]_
  + Misra-Gries Sketch [mg82]_
  + F2 Sketch [ams]_ -- DONE
  + Quantile Sketch [myblog]_
  + ...

Above algorithms share several common features, we could therefore specify a bunch of
common methods, here are some.

.. code-block:: python

   class Sketch(object):
      """
      Interface for Sketch.
      """
      @abstractmethod
      def processBatch(self, *args, **kwargs):
         """
         Summarize data stream in batch mode.
         """
         raise NotImplemented()

      @abstractmethod
      def processItem(self, *args, **kwargs):
         """
         Summarize one item in a data stream.
         """
         raise NotImplemented()

      @abstractmethod
      def estimate(self, *args, **kwargs):
         """
         Estimate properties of given item/key.
         """
         raise NotImplemented()

      @abstractmethod
      def merge(self, *args, **kwargs):
         """
         Merge compatible sketches.
         """
         raise NotImplemented()

      @abstractmethod
      def __add__(self, other):
         return self.merge(other)


Data Stream
------------

Any **iterable** object with **hashable** elements can be considered as a data stream. Here are some examples.

* a list of integers: :code:`[1, 10, 20, 1, 5]`
* a generator that yields tuples, see the instance :code:`dataStream` as follows,

.. code-block:: python
   
   import random

   def demoGen(N = 1000):
       i = 0
       while i < N:
           yield random.randint(0, 10);
           i += 1

   dataStream = demoGen()

* a tuple of strings: :code:`('fix', 'the', 'bug', please', '...')`
* a string: :code:`'abcdefgdahfahdfajkhfkahfsahfjksfhjk'`
* many more


Summarize the data stream
-------------------------
Many algorithms that are popular to summarize data streams are included
in the module **streamlib**. We give some examples to show their basic usage.

Count-Min Sketch
#################
Count-Min sketch [cm05]_ is used to summarize the data stream and estimate the frequency of each element in the data stream. This sketch give high accurate estimation to heavy hitters (elements that have high frequencies) while relatively large error may induced for light elements. See following example for the basic usage.

.. code-block:: python

    from streamlib import CountMin
    cm = CountMin() # create a instance of CountMin, see document for more detail
    cm.processBatch([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4])
    for i in range(5):
	print 'Estimated frequency of', i, 'is', cm.estimate(i)

result of above code,::

	Estimated frequency of 0 is 4
	Estimated frequency of 1 is 6
	Estimated frequency of 2 is 1
	Estimated frequency of 3 is 2
	Estimated frequency of 4 is 1


An instance of `CountMin` can be initialized by two parameters, see docs for detail.


Documents
---------
`Official Document <http://xmerge.me/StreamLib/>`_.

Dependencies
------------------
* Python = 2.x (x >= 6).
* mmh3 >= 2.0


TODO
---------------
* Try to use CPython to speed up the implementation.
* Add more streaming algorithms.
* Minimize dependencies.

Bibliography
-------------
.. [ccfc04] Charikar, Moses, Kevin Chen, and Martin Farach-Colton. "Finding frequent items in data streams." Automata, Languages and Programming. Springer Berlin Heidelberg, 2002. 693-703.

.. [ams] Alon, Noga, Yossi Matias, and Mario Szegedy. "The space complexity of approximating the frequency moments." Proceedings of the twenty-eighth annual ACM symposium on Theory of computing. ACM, 1996.

.. [bjkst] Bar-Yossef, Ziv, et al. "Counting distinct elements in a data stream." Randomization and Approximation Techniques in Computer Science. Springer Berlin Heidelberg, 2002. 1-10.

.. [cm05] Cormode, Graham, and S. Muthukrishnan. "An improved data stream summary: the count-min sketch and its applications." Journal of Algorithms 55.1 (2005): 58-75.

.. [mg82] Misra, Jayadev, and David Gries. "Finding repeated elements." Science of computer programming 2.2 (1982): 143-152.

.. [myblog] http://jiecchen.github.io/blog/2014/08/13/quantile-sketch/


Maintainer
-----------
* `Jiecao Chen <chenjiecao@gmail.com>`_ (currently supported by NSF Grant CCF-1525024)

Other contributors
---------------
* `Qin Zhang <qzhangcs@indiana.edu>`_
* `Rachel Lowden <ralowden@imail.iu.edu>`_


