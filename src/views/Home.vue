<template>
    <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-6">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid grid-cols-3 items-center text-center pb-2">
            <router-link to="/" class="text-black font-bold text-2xl px-3 py-2 bg-gray-100 m-3 rounded-3xl hover:bg-gray-200 hover:text-gray-900 transition-all ease-in-out cursor-pointer">Home</router-link>
            <router-link to="/stats" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Stats</router-link>
             <router-link to='tests' class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Tester</router-link>
          </div>
          <div class="w-full h-2 bg-gray-400 rounded-xl mb-14 mt-2"></div>
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
            <div :class="analyzing ? 'p-1 text-center w-full' : 'hidden'">
              <img class="object-contain h-60 w-full" src='/img/loading.gif' />
              <div class="text-gray-500 font-mono text-2xl transform transition-all animate-pulse">Running Analysis...</div>
            </div>
            <div :class="analyzing ? 'hidden' : 'p-1 w-full max-w-xl overflow-y-scroll'">
              <div v-if="result != null" class="p-4 pb-0 text-3xl text-gray-400 font-extrabold">Result:</div>
              <div v-if="result != null" class="p-5">
                <div class="p-4 pl-5 pr-5 text-gray-400 w-full bg-gray-900 bg-opacity-30 rounded-3xl border-2 border-gray-900 transform transition-all hover:scale-105 cursor-pointer hover:border-gray-600">
                    <div class="grid grid-cols-2 gap-4">
                      <h3>Query: <span class="font-extrabold ">{{result.query}}</span></h3>
                      <div class="text-right text-gray-600"><h4>{{result.timestamp}}</h4></div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 pt-2">
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Sample Size</h1>
                        <h1 class="font-extrabold text-2xl">{{result.size}}</h1>
                      </div>
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Avg. Score</h1>
                        <h1 :class="result.overall_sentiment == 'neutral' ? 'font-extrabold text-2xl text-gray-500' : result.overall_sentiment == 'positive' ? 'font-extrabold text-2xl text-green-accent-700' : 'font-extrabold text-2xl text-red-accent-700'">{{result.avg_score.toFixed(3)}}</h1>
                      </div>
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Sentiment</h1>
                        <h1 class="font-extrabold text-2xl">{{result.overall_sentiment}}</h1>
                      </div>
                    </div>
                  </div>
              </div>
              <div class="w-full border-2 rounded-xl m-4 border-gray-800"></div>
              <div class="p-4 pb-0 text-3xl text-gray-400 font-extrabold">Past Results:</div>
              <ul id="saved_items" class="text-gray-100 p-4">
                <li v-for="item in saved" :key="item.timestamp" class="p-2" @click="get_tweets(item.timestamp)">
                  <div class="p-4 pl-5 pr-5 text-gray-400 w-full bg-gray-900 bg-opacity-30 rounded-3xl border-2 border-gray-900 transform transition-all hover:scale-105 cursor-pointer hover:border-gray-600">
                    <div class="grid grid-cols-2 gap-4">
                      <h3>Query: <span class="font-extrabold ">{{item.query}}</span></h3>
                      <div class="text-right text-gray-600"><h4>{{item.timestamp}}</h4></div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 pt-2">
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Sample Size</h1>
                        <h1 class="font-extrabold text-2xl">{{item.size}}</h1>
                      </div>
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Avg. Score</h1>
                        <h1 :class="item.overall_sentiment == 'neutral' ? 'font-extrabold text-2xl text-gray-500' : item.overall_sentiment == 'positive' ? 'font-extrabold text-2xl text-green-accent-700' : 'font-extrabold text-2xl text-red-accent-700'">{{item.avg_score.toFixed(3)}}</h1>
                      </div>
                      <div class="pt-2 grid grid-cols-1 text-center text-sm">
                        <h1 class="text-gray-500 font-extrabold text-xs">Sentiment</h1>
                        <h1 class="font-extrabold text-2xl">{{item.overall_sentiment}}</h1>
                      </div>
                    </div>
                  </div>
                  <!-- {{ item.query }}, {{ item.size }}, {{ item.avg_score }}, {{ item.avg_rounded_polarity }}, {{ item.timestamp }} -->
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex bg-gray-900 bg-opacity-20">
        <div class="relative w-auto my-6 mx-auto max-w-4xl">
          <!--content-->
          <div class="border-2 border-gray-900 rounded-3xl shadow-lg relative flex flex-col w-full bg-gray-900 text-white outline-none focus:outline-none bg-opacity-10 backdrop-filter backdrop-blur-lg">
            <!--header-->
            <div class="flex items-start justify-between p-5 border-b border-solid border-gray-500 rounded-t">
              <h3 class="text-3xl pt-1">
                Query: <span class="font-extrabold pl-2">{{modalData.query}}</span>
              </h3>
              <button class="p-1 ml-auto bg-transparent border-0 text-white float-right text-3xl leading-none font-semibold outline-none focus:outline-none" @click="showModal = false">
                <span class="bg-transparent text-white opacity-50 text-3xl block outline-none focus:outline-none">
                  ×
                </span>
              </button>
            </div>
            <!--body-->
            <div class="relative p-6 flex-auto">
              <div class="text-2xl p-3 text-gray-400 w-full text-center">{{modalData.timestamp}}</div>
              <div class="grid grid-cols-3 gap-4 pt-2">
                  <div class="pt-2 grid grid-cols-1 text-center text-sm">
                    <h1 class="text-gray-500 font-extrabold text-lg">Sample Size</h1>
                    <h1 class="font-extrabold text-5xl">{{modalData.size}}</h1>
                  </div>
                  <div class="pt-2 grid grid-cols-1 text-center text-sm">
                    <h1 class="text-gray-500 font-extrabold text-lg">Avg. Score</h1>
                    <h1 :class="modalData.overall_sentiment == 'neutral' ? 'font-extrabold text-5xl text-yellow-accent-700' : modalData.overall_sentiment == 'positive' ? 'font-extrabold text-5xl text-green-accent-700' : 'font-extrabold text-5xl text-red-accent-700'">{{modalData.avg_score.toFixed(3)}}</h1>
                  </div>
                  <div class="pt-2 grid grid-cols-1 text-center text-sm">
                    <h1 class="text-gray-500 font-extrabold text-lg">Sentiment</h1>
                    <h1 class="font-extrabold text-5xl">{{modalData.overall_sentiment}}</h1>
                  </div>
                </div>
                <div class="mt-10 pl-9 pr-10 pb-3 font-extrabold text-2xl text-gray-400">Tweets:</div>
                <div class="pl-8 pr-8 pb-6 max-h-96 overflow-y-scroll">
                  <div class="border-b p-4" v-for="tweet in modalData.tweets" :key="tweet.text">
                    {{tweet.text}}
                    <div class="pt-4 font-mono text-xl">Sentiment Score: 
                      <span :class="tweet.analysis.compound >= 0.05 ? 'font-bold text-green-accent-700' : tweet.analysis.compound <= -0.05 ? 'font-bold text-red-accent-700' : 'text-yellow-accent-700 font-bold'">{{tweet.analysis.compound.toFixed(3)}}</span></div>
                  </div>
                </div>
            </div>
            <!--footer-->
            <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
            
              <!-- <button class="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
                Save Changes
              </button> -->
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

export default {
  data: () => ({
    base_url: 'http://localhost:5000',
    search_query: '',
    result: null,
    analyzing: false,
    saved: [],
    showModal: false,
    modalData: null
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
      this.result = null

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
    },
    async get_tweets(timestamp) {
      const path = this.base_url + '/find'

      const res = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          timestamp: timestamp,
        }) 
      });

      const data = await res.json()
      this.modalData = data
      this.showModal = true
    },
  }
}
</script>
