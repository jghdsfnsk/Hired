import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import JobsView from '../views/JobsView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignupView.vue'
import JobDetailView from '../views/JobDetailView.vue'
import JobApplyView from '../views/JobApplyView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/jobs',
    name: 'jobs',
    component: JobsView
  },
  {
    path: '/:username/:job_slug',
    name: 'jobsdetail',
    component: JobDetailView
  },
  {
    path: '/:username/:job_slug/apply',
    name: 'jobapply',
    component: JobApplyView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/log-in',
    name: 'login',
    component: LoginView
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignUpView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireLogin && !localStorage.getItem('token')) {
    next({ name: 'login', query: {to: to.path} })
  } else {
    next()
  }
})


export default router
