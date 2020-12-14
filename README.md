# Python Fundamentals

### **Objective:**
* To complete the method stubs in each of the provided python modules
	* `calculator.py`
	* `predicator.py`
	* `string_manipulator.py`

### **Purpose:**
* To establish familiarity with
    * [method signatures and return statements]()
    * [primitive data-types]()
    * [class and object-definition]()
    * [unit-testing]()
    * [arrays]()
    * [for loops]()
	
### **Instructions:**

1. Fork this Repository
    * [fork](https://help.github.com/articles/fork-a-repo/) this repository to your personal github account 
    * [clone](https://help.github.com/articles/cloning-a-repository/) **your** `forked` repository to your local machine.
    * Complete steps 2 and 3  
    * `git add` your changes to the list of your `commited` files.
    * `git commit` your added files to the list of your `staged` files.
    * `git push` your staged files to your remote repository.
    * submit a `pull request` which compares Perscholas `master` to your `master`.
2. Begin by first ensuring the `main` method in your `perscholas_rocks.py` module prints `"Perscholas Rocks!"` upon execution.  
3. Complete each of the method stubs in each of the `main` classes provided.
    * `main` classes are located in `src.main.java.com.github.perscholas.java_fundamentals`
    * There are comments above each method stub to describe the expected behavior.
4. Upon completion, open and run the `TestSuite` class to ensure that all tests have 100% success.
    * `TestSuite` is located in `src.main.java.com.github.perscholas.java_fundamentals`

## Predicate Utilities
* A _predicate_ is a clause which states something about a subject. (_e.g., **is assigning**_ in _"Leon **is assigning** homework"_)
* Ensure each of the test cases passes successfully in the class [predicator_test.py](./src/test/predicator_test.py) by completing each of the method stubs in the class [predicator.py](./src/main/predicator.py).
* Method Stubs to be completed
	* `is_greater_than_5(some_value)`
	* `is_greater_than_8(some_value)`
    * `is_less_than_4(some_value)`
    * `is_less_than_1(some_value)`

## Math Utilities
* Ensure each of the test cases passes successfully in the class [calculator_test.py](./src/test/calculator_test.py) by completing each of the method stubs in the class [calculator.py](src/main/calculator.py).
* Method Stubs to be completed	
	* `add(first_value, second_value)`
	* `subtract(first_value, second_value)`
	* `divide(first_value, second_value)`
	* `multiply(first_value, second_value)`


## String Utilities
* Ensure each of the test cases passes successfully in the class [string_evaluator_test.py](./src/test/string_evaluator_test.py) by completing each of the method stubs in the class [string_evaluator.py](src/main/string_evaluator.py).
* Method Stubs to be completed
    * `get_hello_world()`
    * `concatenate(first_value, second_value)`
    * `substring_inclusive(string_to_fetch_from, starting_index, ending_index)`
    * `substring_exclusive(string_to_fetch_from, starting_index, ending_index)`
    * `compare(first_value, second_value)`
    * `get_middle_character(string_to_fetch_from)`
    * `get_first_word(string_to_fetch_from)`
    * `get_second_word(string_to_fetch_from)`
    * `reverse(string_to_reverse)`