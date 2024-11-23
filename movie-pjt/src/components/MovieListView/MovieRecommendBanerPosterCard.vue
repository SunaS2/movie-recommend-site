<!-- <template>
  <div>
    <div>
      <img :src="store.getImgUrl(movie.poster_path, 200)" alt="" />
    </div>
    <h4>{{ movie.title_kr }}</h4>
    <h5>{{ movie.title }}</h5>
  </div>
</template> -->
<template>
  <div class="card-container">
    <div class="movie-card">
      <div>
        <img :src="store.getImgUrl(movie.poster_path, 200)" alt="" class="card-img" />
      </div>
      <div class="card-content">
        <h4 class="card-title">{{ movie.title_kr }}</h4>
        <h5 class="card-subtitle">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";

const store = useMovieStore();
defineProps({
  movie: Object,
});
</script>

<style scoped>
.movie-card {
  width: 200px;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* 카드 이미지 */
.card-img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

/* 카드 내용 */
.card-content {
  padding: 1rem;
  text-align: center;
}

.card-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.card-description {
  font-size: 0.9rem;
  color: #666666;
}

/* 호버 효과 */
.movie-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}
</style>
