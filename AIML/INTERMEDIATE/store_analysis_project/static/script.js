Papa.parse("Sample%20-%20Superstore.csv", {
    download: true,
    header: true,
    skipEmptyLines: true,

    complete: function (results) {

        let data = results.data;

        let totalSales = 0;
        let totalProfit = 0;
        let categorySales = {};

        data.forEach(row => {

            let sales = parseFloat(row["Sales"]) || 0;
            let profit = parseFloat(row["Profit"]) || 0;
            let category = row["Category"] || "Unknown";

            totalSales += sales;
            totalProfit += profit;

            if (!categorySales[category]) {
                categorySales[category] = 0;
            }

            categorySales[category] += sales;
        });

        // Update UI
        document.getElementById("sales").innerText = "₹ " + totalSales.toFixed(2);
        document.getElementById("profit").innerText = "₹ " + totalProfit.toFixed(2);

        // Category list
        let list = document.getElementById("categoryList");

        for (let cat in categorySales) {
            let li = document.createElement("li");
            li.innerText = cat + " : ₹ " + categorySales[cat].toFixed(2);
            list.appendChild(li);
        }
    }
});
