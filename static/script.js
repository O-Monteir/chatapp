// Function to simulate typing indicator
function showTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.style.display = 'block';
    }
}

// Function to hide typing indicator and display bot's message

function hideTypingIndicatorAndShowBotMessage(botMessage) {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
      typingIndicator.style.display = 'none';
  
      // Display bot's message
      const chatContainer = document.querySelector('.msger-chat');
      const botMessageElement = document.createElement('div');
      botMessageElement.classList.add('msg', 'left-msg', 'bot-message'); // Add a class to style bot messages differently
      botMessageElement.innerHTML = `
        <img class="msg-img" src="../static/images/bot.png" alt="Ella's Image">
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">Ella</div>
            <div class="msg-info-time">${getCurrentTime()}</div>
          </div>
          <div class="msg-text">${botMessage}</div>
        </div>
      `;
      chatContainer.appendChild(botMessageElement);
    }
}

// Example: Event listener for form submission
const form = document.querySelector('.msger-inputarea');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const userInput = document.querySelector('.msger-input').value;

    const chatContainer = document.querySelector('.msger-chat');
    const userMessageElement = document.createElement('div');
    userMessageElement.innerHTML = `
        <div class="msg right-msg">
            <div class="msg-bubble">
                <div class="msg-info">
                    <div class="msg-info-name">You</div>
                    <div class="msg-info-time">${getCurrentTime()}</div>
                </div>
                <div class="msg-text">${userInput}</div>
            </div>
        </div>
    `;
    chatContainer.appendChild(userMessageElement);

    showTypingIndicator();

    // Fetch actual bot response from the backend using AJAX
    fetch('/get_bot_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.bot_response;
        hideTypingIndicatorAndShowBotMessage(botResponse);

        // Clear the input field after sending the message
        document.querySelector('.msger-input').value = ''; // Clear input area
    })
    .catch(error => console.error('Error:', error));
});

// Function to get current time (replace this with your preferred time formatting logic)
function getCurrentTime() {
    const now = new Date();
    return now.getHours() + ':' + now.getMinutes();
}
