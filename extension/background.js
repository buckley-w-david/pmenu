const onError = error => console.error(error);

browser.browserAction.onClicked.addListener(() => {
  browser.tabs.query({ currentWindow: true, active: true }).then((tabs) => {
    let tab = tabs[0]; // Safe to assume there will only be one result
    browser.runtime.sendNativeMessage(
      "pmenu",
      tab.url,
    ).then((response) => {
      browser.tabs.sendMessage(tab.id, {
        username: response.username,
        password: response.password,
      });
    }, onError);
  }, onError);
});
