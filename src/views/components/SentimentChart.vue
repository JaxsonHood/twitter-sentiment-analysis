<template>
  <div v-if="testData != null">
    <canvas :id="uuid"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import {v4 as uuidv4} from 'uuid';

export default {
  name: "SentimentChart",
  props: ['testData'],
  data() {
    return {
      uuid: uuidv4()
    };
  },
  mounted() {
    let lab = []
    let dat = []

    for (let i = 1; i <= this.testData.num_runs; i++){
      lab.push(i)
    }

    for (let index in this.testData.runs){
      const run = this.testData.runs[index]
      dat.push(run.avg_score)
    }

    let chartData = {
        type: "line",
        data: {
          labels: lab,
          datasets: [
            {
              label: "Sentiment Score",
              fill: false,
              data: dat,
              backgroundColor: "rgba(71, 183,132,.5)",
              borderColor: "#02baed",
              borderWidth: 4,
            },
          ],
        },
        options: {
          showDatasetLabels : true,
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [{
              gridLines: { zeroLineColor: "#131c2b" },
              scaleLabel: {
                display: true,
                labelString: 'Sentiment',
                fontSize: 18,
              },
              ticks: {
                  fontSize: 16,
                  beginAtZero: false,
                  responsive: true,
                  mainAspectRatio: false,
                  callback: (v) => !!~[-1, 0.05, 1].indexOf(v) ? v : '',
                  min: -1,
                  max: 1,
                  step: 0.1
              }
          }],
          xAxes: [{
              gridLines: { zeroLineColor: "#131c2b" },
              scaleLabel: {
                display: true,
                labelString: 'Run #',
                fontSize: 18,
              },
              ticks: {
                  fontSize: 16,
              }
          }]
          }
        }
    }

    const ctx = document.getElementById(this.uuid);
    new Chart(ctx, chartData);
  },
  methods: {
    generateChartConfig(){
      return null
    },
  }
};
</script>