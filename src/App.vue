<template>
  <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid place-items-center h-full">
            <div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
              <div>
                <p class="inline-block px-3 py-2 mb-4 text-xs font-semibold tracking-wider text-gray-300 uppercase rounded-full bg-gray-900">
                  WELCOME TO
                </p>
              </div>
              <h2 class="max-w-lg mb-2 font-sans text-3xl font-bold leading-none tracking-tight text-gray-100 sm:text-4xl md:mx-auto">
                <span class="relative inline-block">
                  <svg viewBox="0 0 52 24" fill="currentColor" class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-gray-700 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block">
                    <defs>
                      <pattern id="b039bae0-fdd5-4311-b198-8557b064fce0" x="0" y="0" width=".135" height=".30">
                        <circle cx="1" cy="1" r=".7"></circle>
                      </pattern>
                    </defs>
                    <rect fill="url(#b039bae0-fdd5-4311-b198-8557b064fce0)" width="52" height="24"></rect>
                  </svg>
                </span>
                Twitter Sentiment Analyser
              </h2>
              <p class="text-base text-gray-500 md:text-lg">
                Type in a topic below to analyse the most recent 100 tweets about it!
              </p>
            </div>
            <div :class="analyzing ? 'hidden' : 'p-1 w-full max-w-xl text-center'">
              <form class="flex flex-col items-center w-full mb-4 md:flex-row md:px-16" @submit.prevent="submitForm">
                <input
                  placeholder="(ex. Topic, Person, Recent Event)"
                  v-model="search_query"
                  required=""
                  type="text"
                  class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-blue-accent-400 focus:outline-none focus:shadow-outline"
                />
                <button
                  type="submit"
                  class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded-2xl shadow-md md:w-auto bg-green-accent-700 hover:border-light-green-accent-700 focus:shadow-outline focus:outline-none"
                >
                  Run
                </button>
              </form>
              <p class="max-w-md mx-auto mb-10 text-xs text-gray-600 sm:text-sm md:mb-16">
                Review previous analysis below!!
              </p>
            </div>
            <div :class="analyzing ? 'p-1' : 'hidden'">
              <img class="object-contain h-60 w-full" src='/img/loading.gif' />
              <div class="text-gray-500 font-mono text-2xl transform transition-all animate-pulse">Running Analysis...</div>
            </div>
            <div :class="analyzing ? 'hidden' : 'p-1'">
              <div class="text-white p-5">RESULTS: {{ result }}</div>
              <ul id="saved_items" class="text-gray-100 p-4">
                <li v-for="item in saved" :key="item.timestamp" class="p-2">
                  {{ item.query }}, {{ item.size }}, {{ item.avg_polarity }}, {{ item.avg_rounded_polarity }}, {{ item.timestamp }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  data: () => ({
    base_url: 'http://localhost:5000',
    search_query: '',
    result: {},
    analyzing: false,
    saved: []
  }),
  created: async function() {
      const path = this.base_url + '/saved'

      const res = await fetch(path, {method: 'GET',});
      const data = await res.json()

      this.saved = data.data.reverse()
  },
  methods: {
    // submit the form to our backend api
    async submitForm() {
      const path = this.base_url + '/analyse'

      this.analyzing = true

      const res = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: this.search_query,
        }) 
      });

      const data = await res.json()
      this.result = data
      this.loadData()

      setTimeout(() => {
        this.search_query = ''
        this.analyzing = false
      }, 2000);
    },
    async loadData() {
      const path = this.base_url + '/saved'

      const res = await fetch(path, {method: 'GET',});
      const data = await res.json()

      this.saved = data.data.reverse()
      console.log("Reloaded Data")
    }
  }
});
</script>
