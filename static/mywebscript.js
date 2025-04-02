function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // 使用 fetch 发起 POST 请求
    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "text=" + encodeURIComponent(textToAnalyze)
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("system_response").innerHTML = data;
    })
    .catch(error => {
        document.getElementById("system_response").innerHTML = "Error: " + error;
    });
}