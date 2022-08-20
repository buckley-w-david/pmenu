console.log("Starting pmenu!");
browser.runtime.onMessage.addListener((request) => {
  const usernameCandidates = [
    "input[autocomplete=username]",
    "input[autocomplete=email]",
    "input[type=email]",
    "input[type=text]",
  ];
  const passwordCandidates = [
    "input[type=password][autocomplete=current-password]",
    "input[type=password][autocomplete=password]",
    "input[type=password]",
  ];

  // TODO: Try to figure out which one to use if there are multiple results
  let passwordInput;
  let usernameInput;

  for (let query of passwordCandidates) {
    passwordInput = document.querySelector(query);
    if (passwordInput !== null) {
      break;
    }
  }
  if (passwordInput === null) {
    console.log("can't find password field!");
    return;
  }

  let form = passwordInput.closest("form");
  if (form !== null) {
    for (let query of usernameCandidates) {
      usernameInput = form.querySelector(query);
      if (usernameInput !== null) {
        break;
      }
    }
    // TODO: Try to figure out which one to use if there are multiple results
    if (usernameInput !== null) {
      usernameInput.value = request.username;
    }
  } else {
    // TODO: Fancier huristics for finding username field?
  }

  passwordInput.value = request.password;
});
