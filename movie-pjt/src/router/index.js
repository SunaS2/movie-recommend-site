import { createRouter, createWebHistory } from 'vue-router'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetail from '@/views/MovieDetailView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import VocaNote from '@/views/VocaNoteView.vue'
import { useMovieStore } from '@/stores/movie'
import WishMovieListView from '@/views/WishMovieListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/:movieid',
      name:'movie-detail',
      component: MovieDetail
    },
    {
      path:'/login',
      name:'login',
      component: LogInView
    },
    {
      path:'/signup',
      name:'signup',
      component: SignUpView
    },
    {
      path:'/vocanote',
      name:'vocanote',
      component: VocaNote
    },
    {
      path:'/myprofie',
      name:'profile',
      component: ProfileView
    },
    {
      path:'/mywishmovies',
      name:'wishmovies',
      component:WishMovieListView
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  // 앞으로 로그인 권한이 필요한 곳이라면 로그인이 필요하다고 알려주고
  // 로그인 창으로 보내기
})
export default router
