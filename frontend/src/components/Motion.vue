<template>
<div class="parentContainer">
  <div class="motionButtons">
    <voting :choice="motion.choice" :votes="motion.votes" :id="id"/>
    <favourite v-show="isAuth" :motion="id"/>
  </div>
  <p>Added on {{motion.created_at?.split('T')[0]}}</p>
  <span class="motion-text">{{motion.topic}}</span>
  <div class="line"></div>
  <ul class="tags">
    <li v-on:click="getFilteredMotions(category)" @click="toggleSelected"
 class="tag" v-for="category in motion.category" :key="category">
      <span class="tag-text"><img  v-if="category === tags" v-on:click="removeFilter()" src="/x.svg"/>{{ categoriesDictionary[category] }}</span>
    </li>
  </ul>
  <div v-if="motions.length > 0 && tags" class="line"></div>
  <motion-list v-if="motions.length > 0 && tags" type="getCategoryMotions" :headers="false" :propsMotions="motions" :hideAll="false" title="Motions:"/>
</div>
</template>

<script>
  import Favourite from './Favourite.vue'
  import Voting from './Voting.vue'
  import MotionList from './MotionList.vue'

  export default {
    data() {
      return {
        isAuth: false,
        categoriesDictionary: {},
        tags: null,
        motions: []
      }
    },
    components: {
      Voting,
      Favourite,
      MotionList
    },
     props: ['id', 'motion'],
    methods: {
      async getFilteredMotions(category) {
        const response = await this.$store.dispatch('getCategoryMotions', {page:1, filters: "category="+category})
        this.tags =  this.tags === category ? null : category
        this.motions = response.results;
      }
    },
    removeFilter () {
      this.tags = null;
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      const categoryArray = await this.$store.dispatch('getMotionAttributes', {type: 'categories'})
      categoryArray.forEach(category => {
        this.categoriesDictionary[category.id] = category.value
      });

    }
  }

</script>

<style scoped lang="scss">

.parentContainer {
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  padding: 20px;
  margin-top: 100px;
  margin-bottom: 40px;

  @media (min-width: 992px) {
    padding: 40px;
  }

  p {
    font-family: "IBM Plex Mono";
    font-size: 14px;
    margin-bottom: 10px;
    margin-top: 40px;

    @media (min-width: 992px) {
      font-size: 18px;
    }
  }
}
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }
  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }
  .tags {
    list-style: none;
    margin-top: 20px;
    overflow: hidden;
    padding: 0;
    cursor: pointer;
  }
  .tag {
    display: inline-block;
    padding-left: 10px;
    padding-right: 10px;
    margin: 10px;
    border-radius: 14px;
    border: 2px solid #3098f3;
    &.selected {
      background-color: #3098f3;
    }
  }
  .tag-text {
    color: #000000;
    font-family: "IBM Plex Mono - Semi Bold Italic";
    font-size: 14px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 18px;
    text-align: center;
  }

  .motion-text {
    /* Style for "EU member" */
    color: #252525;
    font-family: Poppins;
    font-size: 32px;
    line-height: 48px;

    @media (min-width: 992px) {
      font-size: 48px;
      line-height: 60px;
    }
  }

</style>
