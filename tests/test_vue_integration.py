def test_text_is_show(driver):
    driver.get('http://localhost:5000/views/sample')
    assert 'Welcome to Your Vue.js App' in driver.page_source
