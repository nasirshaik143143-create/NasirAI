function startVoice() {
    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("userInput").value = text;
    };

    recognition.onerror = function() {
        alert("Voice input error");
    };
}