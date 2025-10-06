class Range:
    # a simple range class that can be used to represent a range of values
    def __init__(self, start=None, stop=None, step=1):
        if start is None and stop is None:
            # Default constructor (empty range 0 to 0)
            self._start = 0
            self._stop = 0
            self._step = 1
            self._length = 0
            #length is 0 because there are no elements in the range

        elif isinstance(start, Range):
            # Copy constructor
            self._start = start._start
            self._stop = start._stop
            self._step = start._step
            self._length = start._length
            # if the arguments is itself range object, copy its values
            # new object with same data, but a different reference in memory

        elif isinstance(start, int):
            # Parameterized constructor
            if stop is None:   
                stop = start
                start = 0
                # if start is an int, we assume it's the stop value and set start to 0
            
            self._validate_step(step)
            self._start = start
            self._stop = stop
            self._step = step
            self._length = self._compute_length(start, stop, step)
            # self.validate_step(step) checks if step is valid (non-zero integer)
            # compute_length calculates how many elements are in the range
        else:
            raise TypeError("Invalid arguments: must be None, Range, or int")
    
    def _compute_length(self, start, stop, step):
        #def _compute_length(self,only): can be used also for more abstractness
     if step > 0:
        if start >= stop:
            return 0
        return max(0, (stop - start + step - 1) // step)
     else:
         if start <= stop:
             return 0
         return max(0, (start - stop + (-step) - 1) // (-step))
     # max(0, ...) ensures that length is non-negative
        
    def __len__(self):
        return self._length
    # Returns the number of elements in the range
    def __getitem__(self, index):
        self._index_validation(index)
        return self._start + index * self._step
    # formula to get the element at index
    def __str__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"
    def __repr__(self):
       return self.__str__()
    
    def _validate_step(self, step):
        if not isinstance(step, int):
            raise TypeError("Step must be an integer")
        if step == 0:
            raise ValueError("Step cannot be zero")
        # if step is not an integer, raise TypeError
        # if step is zero, raise ValueError
    def _index_validation(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            index += self._length
        if index < 0 or index >= len(self):
            raise IndexError("Index has to be less than length and non-negative")
        # if index is not an integer, raise TypeError
        # if index is negative, convert it to positive by adding length
        # if index is out of bounds, raise IndexError
