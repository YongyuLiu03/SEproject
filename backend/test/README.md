## To test recommend functionality
    ```bash
    git clone https://github.com/YongyuLiu03/SEproject.git
    cd SEproject/backend
    python3 -m test.test_recommend
    ```

    There are 12 test cases in total. For three general scenarios: A cs major junior, A newly entered freshman, and A finance major junior.
    Each scenario has 4 tests that test the intense mode/non-intense mode and chinese/internation student.
    Clearly the first two student can finish their graduation and the third can not transfer to CS major anymore. So, this test the first two
    scenarios should return True for graduation and the last one should return False.

    We do not test on the recommended courses since we added randomness in the recommendation.


## To test parse functionality
    ```bash
    git clone https://github.com/YongyuLiu03/SEproject.git
    cd SEproject
    python -m backend.test.test_parse
    ```

    There are six test cases. For detail information, you could refer to this [document](https://docs.google.com/document/d/1PjTqKO9xqlQ01Nr9J-HbJ1ROrG4NQ2DZoGMmcPNhbaY/edit)
