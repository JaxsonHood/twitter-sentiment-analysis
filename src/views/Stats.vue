<template>
    <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-6">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid grid-cols-3 items-center text-center pb-2">
            <router-link to="/" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400 ">Analyser</router-link>
            <router-link to="/stats" class="text-black font-bold text-2xl px-3 py-2 bg-gray-100 m-3 rounded-3xl hover:bg-gray-200 hover:text-gray-900 transition-all ease-in-out cursor-pointer">Stats</router-link>
             <router-link to='tests' class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Tester</router-link>
          </div>
          <div class="w-full h-2 bg-gray-400 rounded-xl mb-8 mt-2"></div>
          <div class="text-white font-bold p-1">
            <div class="font-semibold text-gray-400">Filter By Query:</div>
            <div class="flex flex-wrap pt-3 pb-4 text-xl">
              <div v-for="query in queries" :key="query" :class="selected == query ? 'px-3 py-1 m-1 bg-white text-black rounded-2xl cursor-pointer': 'px-3 py-1 m-1 bg-gray-900 rounded-2xl cursor-pointer'" @click="filterByQuery(query)">{{query}}</div>
            </div>
          </div>
          <div class="text-3xl font-extrabold text-gray-200 p-2 mb-2">Past Results:</div>
          <div v-if="!isFiltering" class="grid grid-cols-1 p-2">
            <div v-for="result in tests" :key="result.runs[0].timestamp">
              <PreviousResults :result="result" />
            </div>
          </div>
          <div v-if="isFiltering" class="grid grid-cols-1 p-2">
            <div v-for="result in filteredTests" :key="result.runs[0].timestamp">
              <PreviousResults :result="result" />
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import PreviousResults from './components/PreviousResults.vue'

export default {
  components: { PreviousResults },
  data: () => ({
    base_url: 'http://localhost:5000',
    tests: {},
    filteredTests: {},
    isFiltering: false,
    queries: [],
    selected: ""
  }),
  created: async function() {
    await this.get_data()
  },
  methods: {
    async get_data(){
      const path = this.base_url + '/interval_saved'

      const res = await fetch(path, {method: 'GET',});
      const data = await res.json()

      let keys = []
      let queries = []

      Object.keys(data).forEach(function(key) {
        keys.push(key)
        queries.push(data[key].runs[0].query)
      });

      let reveredData = {}

      for (let i = keys.length - 1; i >= 0; i--){
        let k = keys[i]
        reveredData[k] = data[k]
      }

      this.tests = reveredData
      this.queries = [...new Set(queries)];
    },
    filterByQuery(query){
      let filteredData = {}

      if (this.selected == query){
        this.isFiltering = false
        this.selected = ""
      } else {
        for (let uuid in this.tests){
          const item = this.tests[uuid]
          const q = item.runs[0].query

          if (q == query){
            filteredData[uuid] = item
          }
        }

        this.filteredTests = filteredData 
        this.isFiltering = true
        this.selected = query
      }
    }
  }
}
</script>
