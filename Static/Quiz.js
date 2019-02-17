// JavaScript source code
$("#personalityQuiz").submit(function (event) {
    event.preventDefault();
    var answers = $(this).serializeArray();

    var scores = {
        result0: 0,
        result1: 0,
        result2: 0,
        result3: 0
    };
    var total = 0;
    var numQuestions = 5;

    for (var answer of answers) {
        scores[answer.value] += 1;
        total += 1;
    }

    var maxResult = "result0";

    for (var result in scores) {
        if (scores[result] > scores[maxResult]) {
            maxResult = result;
        }
    }
    if (total >= numQuestions) {
        if (maxResult === "result0") {
            window.location.href = "https://bme.rutgers.edu/";
        } else if (maxResult === "result1") {
            window.location.href = "https://cbe.rutgers.edu/";
        } else if (maxResult === "result2") {
            window.location.href = "https://www.ece.rutgers.edu/";
        } else {
            window.location.href = "https://cee.rutgers.edu/";
        }
    }
});

function url_redirect(url) {
    var X = setTimeout(function () {
        window.location.replace(url);
        return true;
    }, 300);

    if (window.location = url) {
        clearTimeout(X);
        return true;
    } else {
        if (window.location.href = url) {
            clearTimeout(X);
            return true;
        } else {
            clearTimeout(X);
            window.location.replace(url);
            return true;
        }
    }
    return false;
};