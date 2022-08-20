console.log("Starting pmenu!");
browser.runtime.onMessage.addListener((request) => {
  // TODO: Try to figure out which one to use if there are multiple results
  let passwordInput = document.querySelector("input[type=password]")
  if (passwordInput === null) {
    console.log("can't find password field!")
    return;
  }

  let form = passwordInput.closest('form');
  if (form !== null) {
    // TODO: Try to figure out which one to use if there are multiple results
    let usernameInput = form.querySelector("input[type=text]");
    if (usernameInput !== null) {
      usernameInput.value = request.username;
    }
  } else {
    // TODO: Fancier huristics for finding username field?
  }

  passwordInput.value = request.password;
});
