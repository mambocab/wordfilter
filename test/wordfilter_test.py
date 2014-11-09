import pytest


@pytest.fixture
def wf():
    from lib import wordfilter
    return wordfilter.Wordfilter()


def test_detects_bad_words_in_a_string(wf):
    assert wf.blacklisted('this string contains the word skank')


def test_detects_bad_words_in_a_string_with_capitalization(wf):
    assert wf.blacklisted('this string contains the word SkAnK')


def test_doesnt_find_bad_words_in_a_clean_string(wf):
    assert not wf.blacklisted('this string was clean!')


def test_add_word_to_blacklist(wf):
    wf.add_words('clean')
    assert wf.blacklisted('this string was clean!')


def test_add_word_in_iterable_to_blacklist(wf):
    wf.add_words(('clean',))
    assert wf.blacklisted('this string was clean!')


def test_casing_doesnt_matter_for_added_words(wf):
    wf.add_words('cleaN')
    assert wf.blacklisted('this string was Clean!')


def test_add_multiple_words_to_blacklist(wf):
    wf.add_words(['clean', 'comf'])
    assert wf.blacklisted('this string was clean!')
    assert wf.blacklisted('and i was just getting Comfortable')


def test_clear_blacklist(wf):
    wf.clear_list()
    assert not wf.blacklisted('this string contains the word skank')
    wf.add_words('skAnk')
    assert wf.blacklisted('this string contains the word skank')


def test_module_api(wf):
    from lib import wordfilter
    module_exports = dir(wordfilter)
    assert 'blacklisted' in module_exports
    assert 'clear_list' in module_exports
    assert 'add_words' in module_exports


def test_changing_instance_doesnt_change_module_blacklist(wf):
    from lib import wordfilter
    wf.clear_list()
    assert wordfilter.blacklisted('this string contains the word skank')
    assert not wf.blacklisted('this string contains the word skank')


def test_changing_module_instance_blacklist_doesnt_change_instance(wf):
    from lib import wordfilter
    wordfilter.clear_list()
    assert wf.blacklisted('this string contains the word skank')
