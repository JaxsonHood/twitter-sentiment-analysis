<template>
    <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-6">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid grid-cols-3 items-center text-center pb-2">
            <router-link to="/" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400 ">Home</router-link>
            <router-link to="/stats" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Stats</router-link>
             <router-link to='tests' class="text-black font-bold text-2xl px-3 py-2 bg-gray-300 m-3 rounded-3xl hover:bg-gray-200 hover:text-gray-900 transition-all ease-in-out cursor-pointer">Testing</router-link>
          </div>
          <div class="w-full h-2 bg-gray-400 rounded-xl mb-12 mt-2"></div>
          <div class="text-3xl font-extrabold text-gray-200 p-2 mb-2">New Test:</div>
          <div class="grid place-items-center h-full">
            <div class="w-full bg-gray-900 border-4 border-gray-500 bg-opacity-25 rounded-3xl px-5 py-4 text-white">
              <form class="grid grid-cols-2">
                <div class="mb-1 sm:mb-2">
                  <label for="name" class="inline-block mb-2 font-bold">Query</label>
                   <input
                    placeholder="(ex. Topic, Person, Recent Event)"
                    v-model="search_query"
                    required=""
                    type="text"
                    class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 focus:border-blue-accent-400 focus:outline-none focus:shadow-outline"
                />
                 <div class="grid grid-cols-2 gap-4">
                   <div>
                    <label for="name" class="inline-block mb-2 font-bold">Interval (ex. h:m)</label>
                    <input
                      placeholder="(ex. 00:10)"
                      v-model="interval"
                      required=""
                      type="text"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-blue-accent-400 focus:outline-none focus:shadow-outline"
                    />
                  </div>
                  <div>
                    <label for="name" class="inline-block mb-2 font-bold"># of Runs</label>
                    <input
                      placeholder="(ex. 25)"
                      v-model="num_of_runs"
                      required=""
                      type="number"
                      class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-gray-900 border focus:bg-black border-gray-300 text-white rounded-2xl shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-blue-accent-400 focus:outline-none focus:shadow-outline text-center"
                    />
                  </div>
                 </div>
                </div>
                <div class="grid place-items-center h-full">
                  <div class="px-8 py-3 border-2 border-gray-500 hover:border-gray-900 hover:bg-green-accent-700 text-green-accent-700 hover:text-black rounded-xl transition-all ease-in-out">
                    <font-awesome-icon class="text-3xl" icon="play" />
                  </div>
                </div>
              </form>
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
    interval: '',
    num_of_runs: ''
  }),
}
</script>