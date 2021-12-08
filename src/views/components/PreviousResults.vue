<template>
  <div
    class="
      border-2
      text-white
      px-3
      py-3
      rounded-3xl
      grid grid-cols-8
      gap-2
      border-gray-600
      mb-6
    "
  >
    <div class="col-span-2">
      <div class="rounded-lg px-3 py-2 text-xl">
        <div class="text-sm text-gray-500">Query</div>
        <div class="font-bold">{{ result.runs[0].query }}</div>
        <div class="text-sm text-gray-500 pt-2">Interval</div>
        <div>{{ result.interval_milliseconds / 1000 }}sec</div>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <div class="text-sm text-gray-500 pt-2">Runs</div>
            <div>{{ result.num_runs }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-500 pt-2">Sample #</div>
            <div>{{ result.runs[0].size }}</div>
          </div>
        </div>
        <div class="text-sm text-gray-500 pt-2">Avg. Score</div>
        <div :class="generateAvg(result) >= 0.05 ? 'text-green-accent-700 font-bold' : generateAvg(result) <= -0.05 ? 'text-red-accent-700 font-bold' : 'text-yellow-accent-700 font-bold'">{{generateAvg(result)}}</div>
        <div class="pt-4 p-1 text-xs text-gray-300">{{result.runs[0].timestamp}}</div>
      </div>
    </div>
    <div class="p-1 col-span-6">
      <SentimentChart :testData="result" />
    </div>
  </div>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import SentimentChart from './SentimentChart.vue'

export default {
  components: { SentimentChart },
  name: "PreviousResults",
  props: ["result"],
  data() {
    return {
      uuid: new uuidv4(),
    };
  },
  mounted() {
    
  },
  methods: {
    generateAvg(result) {
      const runs = result.runs
      const size = runs.length
      let total_score = 0

      for (let i = 0; i < size; i++){
          const run = runs[i]
          total_score = total_score + run.avg_score
      }

      return (total_score / size).toFixed(4)
    },
  },
};
</script>