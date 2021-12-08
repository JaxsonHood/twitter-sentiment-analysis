<template>
    <div class="w-screen h-full bg-black min-h-screen">
      <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-6">
        <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-3xl">
          <div class="grid grid-cols-3 items-center text-center pb-2">
            <router-link to="/" class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400 ">Home</router-link>
            <router-link to="/stats" class="text-black font-bold text-2xl px-3 py-2 bg-gray-100 m-3 rounded-3xl hover:bg-gray-200 hover:text-gray-900 transition-all ease-in-out cursor-pointer">Stats</router-link>
             <router-link to='tests' class="text-gray-400 font-bold text-2xl px-3 py-2 bg-black m-3 rounded-3xl hover:text-white transition-all ease-in-out cursor-pointer border-2 border-gray-800 hover:border-gray-400">Tester</router-link>
          </div>
          <div class="w-full h-2 bg-gray-400 rounded-xl mb-12 mt-2"></div>
          <div></div>
        </div>
      </div>
  </div>
</template>

<script>
export default {}
</script>
