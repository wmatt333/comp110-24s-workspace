"""Dictionary Tests Assignment."""

__author__ = "730544766"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case_1() -> None:
    """Tests that the function properly inverts a dictionary made of numbers as strings."""
    test: dict[str, str] = {'1': '2', '3': '4', '5': '6'}
    result = invert(test)
    assert result == {'2': '1', '4': '3', '6': '5'}


def test_invert_use_case_2() -> None:
    """Tests that the function does not mutate the original arguments list."""
    test: dict[str, str] = {'1': '2', '3': '4', '5': '6'}
    result = invert(test)
    assert test == {'1': '2', '3': '4', '5': '6'} != result


def test_invert_edge_case() -> None:
    """Tests that the function works with an empty list."""
    test: dict[str, str] = {}
    result = invert(test)
    assert result == {}


def test_favorite_color_use_case_1() -> None:
    """Tests that the function returns the correct color for a standard list."""
    test: dict[str, str] = {"Jacob": "purple", "Nathan": "green", "Laura": "yellow", "Kayla": "purple"}
    result = favorite_color(test)
    assert result == "purple"


def test_favorite_color_use_case_2() -> None:
    """Tests that the function returns the first color in a tied standard list."""
    test: dict[str, str] = {"Jacob": "green", "Nathan": "green", "Laura": "purple", "Kayla": "purple"}
    result = favorite_color(test)
    assert result == "green"


def test_favorite_color_edge_case() -> None:
    """Tests if the function will still work with empty strings for colors."""
    test: dict[str, str] = {"Jacob": "", "Nathan": "", "Laura": "green", "Kayla": "purple"}
    result = favorite_color(test)
    assert result == ""


def test_count_use_case_1() -> None:
    """Tests if the funtion works with a standard list of different drinks."""
    test: list[str] = ["water", "soda", "tea", "tea", "coffee", "water"]
    result = count(test)
    assert result == {"water": 2, "soda": 1, "tea": 2, "coffee": 1}


def test_count_use_case_2() -> None:
    """Tests if the funtion will not mutate the original list."""
    test: list[str] = ["water", "soda", "tea", "tea", "coffee", "water"]
    result = count(test)
    assert test == ["water", "soda", "tea", "tea", "coffee", "water"] != result


def test_count_edge_case() -> None:
    """Tests if the function will return an empty dictionary when given an empty list."""
    test: list[str] = []
    result = count(test)
    assert result == {}


def test_alphabetizer_use_case_1() -> None:
    """Tests if the function will work with a standard list."""
    test: list[str] = ["happy", "sad", "soap", "high", "good", "cat"]
    result = alphabetizer(test)
    assert result == {"h": ['happy', 'high'], "s": ['sad', 'soap'], "g": ['good'], "c": ['cat']}


def test_alphabetizer_use_case_2() -> None:
    """Tests if the function will work with a standard list that all start with different letters."""
    test: list[str] = ["soap", "high", "good", "cat"]
    result = alphabetizer(test)
    assert result == {"h": ['high'], "s": ['soap'], "g": ['good'], "c": ['cat']}


def test_alphabetizer_edge_case_() -> None:
    """Tests if the function will work with a list of all the same word."""
    test: list[str] = ["soap", "soap", "soap", "soap"]
    result = alphabetizer(test)
    assert result == {"s": ['soap', 'soap', 'soap', 'soap']}


def test_update_attendance_use_case_1() -> None:
    """Tests if the function works when a new person is added to an already existing day."""
    log: dict = {"Thursday": ["Caleb", "David"], "Friday": ["Tyler"]}
    update_attendance(log, "Friday", "Jeff")
    assert log == {'Thursday': ['Caleb', 'David'], 'Friday': ['Tyler', 'Jeff']}


def test_update_attendance_use_case_2() -> None:
    """Tests if the function works when a new person is added to a new day."""
    log: dict = {"Thursday": ["Caleb", "David"], "Friday": ["Tyler"]}
    update_attendance(log, "Wednesday", "Jeff")
    assert log == {'Thursday': ['Caleb', 'David'], 'Friday': ['Tyler'], 'Wednesday': ['Jeff']}


def test_update_attendance_edge_case() -> None:
    """Tests if the function works when an empty string name is used."""
    log: dict = {"Thursday": ["Caleb", "David"], "Friday": ["Tyler"]}
    update_attendance(log, "Friday", "")
    assert log == {'Thursday': ['Caleb', 'David'], 'Friday': ['Tyler', '']}