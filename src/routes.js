import Home from './views/Home.vue'
import Stats from './views/Stats.vue'
import Tests from './views/Tests.vue'
import NotFound from './views/NotFound.vue'

/** @type {import('vue-router').RouterOptions['routes']} */
export let routes = [
  { path: '/', component: Home, meta: { title: 'Home' } },
  { path: '/stats', component: Stats, meta: { title: 'Stats' } },
  { path: '/tests', component: Tests, meta: { title: 'Tests' } },
  { path: '/:path(.*)', component: NotFound },
]
