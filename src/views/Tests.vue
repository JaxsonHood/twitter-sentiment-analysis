<template>
    <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-6">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid grid-cols-3 items-center text-center pb-2">
            <router-link to="/" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400 ">Home</router-link>
            <router-link to="/stats" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Stats</router-link>
             <router-link to='tests' class="text-black font-bold text-2xl px-3 py-2 bg-gray-100 m-3 rounded-3xl hover:bg-gray-200 hover:text-gray-900 transition-all ease-in-out cursor-pointer">Tester</router-link>
          </div>
          <div class="w-full h-2 bg-gray-400 rounded-xl mb-12 mt-2"></div>
          <div class="text-3xl font-extrabold text-gray-200 p-2 mb-2">New Test:</div>
          <div class="grid place-items-center h-full">
            <div class="w-full bg-gray-900 border-4 border-gray-500 bg-opacity-25 rounded-3xl px-5 py-4 text-white">
              <form class="grid grid-cols-12">
                <div class="mb-1 sm:mb-2 col-span-7">
                 <div class="grid grid-cols-9 gap-4">
                  <div class="col-span-6">
                    <label for="name" class="inline-block mb-2 font-bold">Query</label>
                    <input
                      placeholder="(ex. Topic, Person, Recent Event)"
                      v-model="search_query"
                      required=""
                      type="text"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 focus:border-blue-accent-400 focus:outline-none focus:shadow-outline"
                    />
                  </div>
                  <div class="col-span-3">
                    <label for="name" class="inline-block mb-2 font-bold">Sample Size</label>
                    <input
                      placeholder="{10 -> 100}"
                      v-model="sample_size"
                      required=""
                      type="number"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 focus:border-red-accent-400 focus:outline-none focus:shadow-outline"
                    />
                  </div>
                 </div>
                 <div class="grid grid-cols-2 gap-4">
                   <div>
                    <label for="name" class="inline-block mb-2 font-bold">Interval (ex. h:m:s)</label>
                    <input
                      placeholder="(ex. 0:0:10)"
                      v-model="interval"
                      required=""
                      type="text"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-yellow-accent-400 focus:outline-none focus:shadow-outline"
                    />
                  </div>
                  <div>
                    <label for="name" class="inline-block mb-2 font-bold"># of Runs</label>
                    <input
                      placeholder="(ex. 25)"
                      v-model="num_of_runs"
                      required=""
                      type="number"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-green-accent-400 focus:outline-none focus:shadow-outline text-center"
                    />
                  </div>
                 </div>
                </div>
                <div class="grid place-items-center h-full col-span-5">
                  <div v-if="running" class="text-xl font-bold text-gray-400">Completed <span class="pl-1 pr-1 text-2xl text-gray-100 font-extrabold">{{current_run}}/{{num_of_runs}}</span> runs</div>
                  <div v-if="running" class="text-lg font-bold text-gray-400">Next Run <span class="pl-1 pr-1 text-xl text-gray-100 font-extrabold">{{time_left}}</span> sec..</div>
                  <div v-if="running == false" class="px-8 py-3 border-2 border-gray-500 hover:border-gray-900 hover:bg-green-accent-700 text-green-accent-700 hover:text-black rounded-xl transition-all ease-in-out cursor-pointer" @click="run_test()">
                    <font-awesome-icon class="text-3xl" icon="play" />
                  </div>
                  <div v-if="running" class="px-8 py-3 border-2 border-gray-500 hover:border-gray-900 hover:bg-red-accent-700 text-red-accent-700 hover:text-black rounded-xl transition-all ease-in-out cursor-pointer" @click="stop_run(false)">
                    <font-awesome-icon class="text-3xl" icon="stop" />
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="text-3xl font-extrabold text-gray-200 p-2 mb-2 pt-10">Previous Results:</div>
          <div class="grid grid-cols-1 p-2">
            <div v-for="result in previous_tests" :key="result.runs[0].timestamp">
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
    search_query: '',
    interval: '',
    num_of_runs: '',
    current_run: 0,
    sample_size: '',
    interval_result: null,
    time_next: 0,
    time_left: 0,
    running: false,
    done: false,
    previous_tests: {},
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

      Object.keys(data).forEach(function(key) {
        keys.push(key)
      });

      let reveredData = {}

      for (let i = keys.length - 1; i >= 0; i--){
        let k = keys[i]
        reveredData[k] = data[k]
      }

      this.previous_tests = reveredData
    },
    async run_test() {
      if (this.search_query != '' && this.interval.includes(':') && this.num_of_runs != '' && this.sample_size != ''){
        this.running = true

        const hours = parseInt(this.interval.split(':')[0])
        const minutes = parseInt(this.interval.split(':')[1])
        const seconds = parseInt(this.interval.split(':')[2])
        const total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
        const milliseconds = total_seconds * 1000
        
        const uuid = Date.now()
        this.run_loop(milliseconds, this.search_query, parseInt(this.num_of_runs), uuid, parseInt(this.sample_size))

      } else{
        alert("Please fill out all of the information correctly")
      }
    },
    async run_loop(interval, query, runs, uuid, size){
      if (this.running){
        if (runs == parseInt(this.num_of_runs)){
          this.do_count_down((interval / 1000))
          this.run_task(query, uuid, interval, runs, size)
          this.run_loop(interval, query, (runs - 1), uuid, size)
        } else {
          setTimeout(async () => {
            this.get_data()
            this.clear_timeouts()
            this.do_count_down((interval / 1000))
            this.run_task(query, uuid, interval, runs, size)
            if (runs > 1){
              this.run_loop(interval, query, (runs - 1), uuid, size)
            } else {
              this.stop_run(true)
            }
          }, interval);
        }
      }
    },
    do_count_down(seconds){
      this.time_left = seconds
      setTimeout(() => {
        if (seconds > 1){
          this.do_count_down((seconds - 1))
        }
      }, 1000);
    },
    clear_timeouts(){
      var maxId = setTimeout(function() {}, 0);
      for (var i = 0; i < maxId; i += 1) {
        clearTimeout(i);
      }
    },
    async run_task(query, uuid, interval, runs, size){
      const path = this.base_url + '/interval_test'

      const res = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: query,
          uuid: uuid,
          interval: interval,
          runs: runs,
          size: size
        }) 
      });

      const data = await res.json()
      this.interval_result = data
      this.current_run = this.current_run + 1
    },
    stop_run(isClear) {
      this.running = false
      this.done = true

      if (isClear){
        this.search_query = '',
        this.interval = '',
        this.num_of_runs = ''
        this.get_data()
      }
    }
  }
}
</script>