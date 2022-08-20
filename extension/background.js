(() => {
  if (window.isConnected) return;

  let port = chrome.runtime.connectNative('pmenu');
  window.isConnected = true;

  port.onMessage.addListener((response) => {
    browser.tabs.sendMessage(
        response.id,
        {
            username: response.username,
            password: response.password,
        },
    )

  });

  port.onDisconnect.addListener(p => {
    window.isConnected = false;
    console.log('disconnect', p);
  });

  browser.browserAction.onClicked.addListener(() => {
      browser.tabs.query({currentWindow: true, active: true}).then((tabs) => {
          let tab = tabs[0]; // Safe to assume there will only be one result
          message = {
            id: tab.id,
            url: tab.url,
          }
          console.log("Sending: " + tab.url);
          port.postMessage(message);
      }, console.error)
  });
})()
