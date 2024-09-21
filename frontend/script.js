function classify() {
    const form = document.getElementById("classification-form");
    const formData = new FormData(form);

    const data = {};
    formData.forEach((value, key) => {
      data[key] = parseFloat(value);
    });

    let url = "http://127.0.0.1:5000/classify";
    fetch(url, {
      headers: {
        "Content-Type": "application/json",
      },
      method: "post",
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Response from backend was not ok");
        }
        return response.json();
      })
      .then((data) => {
        const classification = data.classification;

        let classificationResult;
        switch (Math.floor(classification)) {
          case 1:
            classificationResult = "Normal";
            document.getElementById("result").className = "result-healthy";
            break;
          case 2:
            classificationResult = "Suspect";
            document.getElementById("result").className = "result-suspect";
            break;
          case 3:
            classificationResult = "Pathological";
            document.getElementById("result").className = "result-pathological";
            break;
          default:
            classificationResult = "Unknown";
            break;
        }
        document.getElementById(
          "result"
        ).innerText = `Classification: ${classificationResult}`;
      })
      .catch((error) => {
        document.getElementById("result").className = "error";
        document.getElementById("result").innerText =
          "An error occurred. Please check input data and try again.";
      });

  }