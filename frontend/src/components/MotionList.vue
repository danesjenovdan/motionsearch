<template>
  <div class="parent-container">
    <div class="header">
      <div class="logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
      </div>
      <div class="header-buttons">
        <router-link to="/motionSuggest" class="btn">Suggest a motion</router-link>
        <router-link to="/login" v-show="!isAuth" class="btn login">Log in</router-link>
      </div>
    </div>
    <div class="line"/>
    <div class="motions-container">
      <div class="motions-title-bar">
        <div>
          <h3>Motions</h3>
          <button class="btn" @click="toggleFilters">Filters</button>
        </div>
        <div class="motions-sort">
          <p>Sort by</p>
          <div class="sort-button">Date Added</div>
          <div class="sort-button">Quality</div>
        </div>
      </div>
      <div class="motions-list" v-for="motion in motions" :key="motion.id">
        <div class="motion-text-container">
          <p class="motions-date">Added on {{motion.created_at}}</p>
          <a :href="'/motion/'+motion.id"><p class="motions-title">{{motion.topic}}</p></a>
        </div>
        <div class="votes">
          <voting :votes="motion.votes"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Voting from './Voting.vue'

  let motions = [];
  let page = 1;
  let refresh = true;
  export default {
    data() {
      return {
        motions,
        page,
        refresh,
        isAuth: false
      }
    },
    components: {
      Voting
    },
    methods: {
      async loadNextPage() {
        try {
          this.page += 1;
          const result = await this.$store.dispatch('getMotions', {page: this.page})
          if(result) this.motions = this.motions.concat(result)
          else this.page -= 1
          this.refresh = true
        } catch (error) {
          this.refresh = true
        }
      },
      handleScroll(e) {
        // compare height of motions-container to window height to enable next scrolling
        let element = document.querySelector('.motions-container')
        if ( element.getBoundingClientRect().bottom < window.innerHeight && this.refresh) {
          this.loadNextPage()
          this.refresh = false
        }
      },
      toggleFilters() {
        this.$emit('toggle-filters')
      }
    },
    mounted() {
      window.addEventListener("scroll", this.handleScroll)
    },
    unmounted() {
      window.removeEventListener("scroll", this.handleScroll)
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      this.motions = await this.$store.dispatch('getMotions', {page: 1})
    }
  }

</script>

<style scoped lang="scss">

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;

  @media (min-width: 768px) {
    justify-content: flex-end;
    padding: 20px;
  }

  @media (min-width: 1200px) {
    padding: 30px;
  }

  .logo {
    @media (min-width: 768px) {
      display: none;
    }

    img {
      height: 40px;
    }
  }
}

.motions-container {
  display: flex;
  flex-direction: column;
  // overflow: hidden;
  padding: 0 20px;
  margin-bottom: 20px;

  @media (min-width: 992px) {
    padding: 0 40px;
  }

  .motions-title-bar {
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid black;

    @media (min-width: 992px) {
      flex-direction: row;
      justify-content: space-between;
    }

    div:nth-child(1) {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;

      @media (min-width: 992px) {
        padding: 20px 0;
      }
    }

    h3 {
      font-size: 16px;
      margin: 0;
      color: #252525;
      font-family: "Poppins";

      @media (min-width: 768px) {
        font-size: 30px;
        line-height: 60px;
      }
    }

    button {
      font-size: 14px;
      letter-spacing: 1px;
      padding: 5px 12px;

      @media (min-width: 768px) {
        display: none;
      }
    }

    .motions-sort {
      display: flex;
      flex-direction: row;
      align-items: center;
      margin-bottom: 10px;

      @media (min-width: 992px) {
        margin-bottom: 0;
      }

      .sort-button, p {
        font-family: "IBM Plex Mono";
        font-size: 12px;
        line-height: 14px;

        @media (min-width: 992px) {
          font-size: 14px;
          line-height: 18px;
        }
      }

      .sort-button {
        border-radius: 20px;
        background-color: rgb(48, 152, 243, 0.2);
        padding: 5px 10px;
        margin-left: 10px;
        cursor: pointer;
        color: #000000;
        font-weight: 700;
        text-transform: uppercase;
      }
    }
  }

  .motions-list {
    border-bottom: 1px solid black;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    // width: 100%;

    .motion-text-container {
      display: flex;
      flex-direction: column;
      color: #252525;

      .motions-date {
        color: #252525;
        font-family: "IBM Plex Mono";
        font-size: 14px;
        font-style: italic;
        line-height: 18px;
        text-align: left;
      }

      .motions-title {
        color: #252525;
        font-family: Poppins;
        font-size: 24px;
      }
    }

    .votes {
      width: 78px;
      height: 78px;
      flex-shrink: 0;
      margin-right: 20px;
      margin-left: 20px;
      background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
    }
  }
}

.share-bar {
  position: relative;
  width: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  padding: 20px;
  // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
  z-index: 2;

  .share-bar-split {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: center;
    &.hidden {
      display: none !important;
    }
  }

  h1 {
      margin-top: 0;
      // width: 100%;
  }

  input {
      margin-left: 20px;
  }
}

.parent-container {
  display: flex;
  margin: 0 auto;
  flex-direction: column;
  justify-content: center;
  align-items: initial;
  overflow-x: auto;
}

.favourite{
  background-image: '../assets/favourite.svg';
}

.motionButtons {
  display: flex;
  justify-content: space-between;
}

.line {
  margin: 0;
  border-top: 1px solid #3098f3;
}

</style>
