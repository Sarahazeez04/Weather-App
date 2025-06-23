function fetchWeather() {
    const city = document.getElementById("city-input").value;
    const apiUrl = `http://localhost:5000/weather?city=${city}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("weather-output").innerText = "Could not fetch weather data. Please try again.";
            } else {
                const weatherOutput = `The current weather in ${data.city} is ${data.temperature}°C and ${data.weather}.`;
                document.getElementById("weather-output").innerText = weatherOutput;

                // Text-to-speech using browser API
                if ('speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(weatherOutput);
                    window.speechSynthesis.speak(utterance);
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("weather-output").innerText = "Error fetching data.";
        });
}
