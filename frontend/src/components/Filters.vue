<template>
  <div>
    <div class="search"><h3>Search for motions</h3></div>
    <div class="filters-container">
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenCategoryFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/topic.svg">
          <span v-if="chosenCategoryFilters.length === 0" data-type="categoryFilter"><i>Themes</i></span>
          <span v-if="chosenCategoryFilters.length > 0">{{ chosenFiltersText(chosenCategoryFilters) }}</span>
        </div>
        <div class="popup-container" id="categoryFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="category in categoryArray" :key="category" >
                <input :id="'category-' + category.id" type='checkbox' :value="{id: category.id, value: category.value}" v-model="categoryFilter"/>
                <label class="popup-text" :for="'category-' + category.id">{{category.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters" data-type="categoryFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenDifficultyFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/difficulty.svg">
          <span v-if="chosenDifficultyFilters.length === 0" data-type="difficultyFilter"><i>Difficulty</i></span>
          <span v-if="chosenDifficultyFilters.length > 0">{{ chosenFiltersText(chosenDifficultyFilters) }}</span>
        </div>
        <div class="popup-container" id="difficultyFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="difficulty in difficultiesArray" :key="difficulty">
                <input :id="'difficulty-' + difficulty.id" :value="{id: difficulty.id, value: difficulty.value}" type='checkbox' v-model="difficultyFilter"/>
                <label class="popup-text" :for="'difficulty-' + difficulty.id">{{difficulty.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters" data-type="difficultyFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenFormatFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/format.svg">
          <span v-if="chosenFormatFilters.length === 0" data-type="formatFilter"><i>Formats</i></span>
          <span v-if="chosenFormatFilters.length > 0">{{ chosenFiltersText(chosenFormatFilters) }}</span>
        </div>
        <div class="popup-container" id="formatFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="format in formatArray" :key="format">
                <input :id="'format-' + format.id" :value="{id: format.id, value: format.value}" type='checkbox' v-model="formatFilter"/>
                <label class="popup-text" :for="'format-' + format.id">{{format.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters"  data-type="formatFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenAgeFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/age.svg">
          <span v-if="chosenAgeFilters.length === 0" data-type="ageFilter"><i>Age</i></span>
          <span v-if="chosenAgeFilters.length > 0">{{ chosenFiltersText(chosenAgeFilters) }}</span>
        </div>
        <div class="popup-container" id="ageFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="age in ageArray" :key="age">
                <input :id="'age-' + age.id" :value="{id: age.id, value: age.value}" type='checkbox' v-model="ageFilter"/>
                <label class="popup-text" :for="'age-' + age.id">{{age.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters"  data-type="ageFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenTypeFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/type.svg">
          <span v-if="chosenTypeFilters.length === 0" data-type="typeFilter"><i>Motion type</i></span>
          <span v-if="chosenTypeFilters.length > 0">{{ chosenFiltersText(chosenTypeFilters) }}</span>
        </div>
        <div class="popup-container" id="typeFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="type in typeArray" :key="type">
                <input :id="'type-' + type.id" :value="{id: type.id, value: type.value}" type='checkbox' v-model="typeFilter"/>
                <label class="popup-text" :for="'type-' + type.id">{{type.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters"  data-type="typeFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box bottom-popup"
          :class="{ 'filters-selected': chosenTrainingFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/focus.svg">
          <span v-if="chosenTrainingFilters.length === 0" data-training="trainingFilter"><i>Training focus</i></span>
          <span v-if="chosenTrainingFilters.length > 0">{{ chosenFiltersText(chosenTrainingFilters) }}</span>
        </div>
        <div class="popup-container" id="trainingFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="training in trainingFocusArray" :key="training">
                <input :id="'training-' + training.id" :value="{id: training.id, value: training.value}" type='checkbox' v-model="trainingFilter"/>
                <label class="popup-text" :for="'training-' + training.id">{{training.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters"  data-type="trainingFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box top-popup"
          :class="{ 'filters-selected': chosenImproPrepFilters.length }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/impro.svg">
          <span v-if="chosenImproPrepFilters.length === 0" data-type="improPrepFilter"><i>Either impro or prep</i></span>
          <span v-if="chosenImproPrepFilters.length > 0">{{ chosenFiltersText(chosenImproPrepFilters) }}</span>
        </div>
        <div class="popup-container" id="improPrepFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="impro in improPrepArray" :key="impro">
                <input :id="'impro-' + impro.id" :value="{id: impro.id, value: impro.value}" type='checkbox' v-model="improPrepFilter"/>
                <label class="popup-text" :for="'impro-' + impro.id">{{impro.value}}</label>
              </div>
            </div>
            <div class="popup-apply" :onclick="toggleFilters"  data-type="improPrepFilter">Apply</div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div
          class="filter-box top-popup"
          :class="{ 'filters-selected': chosenKeywordFilters }"
          @click="toggleSelected"
          v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/keyword.svg">
          <span data-type="keywordFilter"><i>Keyword</i></span>
        </div>
        <div class="popup-container" id="keywordFilter" @click.stop>
          <div class="popup-box">
            <span class="keyword-text">Enter keyword(s), separated by a comma</span>
            <div class="keyword-container">
              <input class="" v-model="keywordFilter"/>
            </div>
            <div class="keyword-apply">
              <span :onclick="clearKeywords">Clear all</span>
              <div class="popup-apply" :onclick="toggleFilters"  data-type="keywordFilter">Apply</div>
            </div>
          </div>
          <div class="popup-arrow">
          </div>
        </div>
      </div>
      <div @click="randomMotion" :disabled="isDisabled" :class="['filter-box', 'randomFilterBox']">
        <div class="content">
          <img src="../assets/random.svg">
          <span ><i>Show me a random motion</i></span>
        </div>
      </div>
    </div>
    <div class="apply-button">
      <button class="btn" @click="closeFilters">Apply</button>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      categoryArray: [],
      difficultiesArray: [],
      ageArray: [],
      formatArray: [],
      typeArray: [],
      trainingFocusArray: [],
      improPrepArray: [],
      ageFilter: [],
      categoryFilter: [],
      formatFilter: [],
      improPrepFilter: [],
      difficultyFilter: [],
      typeFilter: [],
      trainingFilter: [],
      keywordFilter: ''
    }
  },
  computed: {
    chosenCategoryFilters () {
      return this.$store.getters.getFilters.categoryFilter || [];
    },
    chosenDifficultyFilters () {
      return this.$store.getters.getFilters.difficultyFilter || [];
    },
    chosenFormatFilters () {
      return this.$store.getters.getFilters.formatFilter || [];
    },
    chosenAgeFilters () {
      return this.$store.getters.getFilters.ageFilter || [];
    },
    chosenTypeFilters () {
      return this.$store.getters.getFilters.typeFilter || [];
    },
    chosenTrainingFilters () {
      return this.$store.getters.getFilters.trainingFilter || [];
    },
    chosenImproPrepFilters () {
      return this.$store.getters.getFilters.improPrepFilter || [];
    },
    chosenKeywordFilters () {
      return this.$store.getters.getFilters.keywordFilter;
    },
    isDisabled () {
      return this.$store.getters.motion_length > 0
    }
  },
  directives: {
    outside: {
      beforeMount(el, binding, vnode) {
        el.clickOutsideEvent = function(event) {
          if (!(el === event.target || el.contains(event.target))) {
            binding.value(event, el);
          }
        };
        document.body.addEventListener('click', el.clickOutsideEvent);
      },
      unmounted(el) {
        document.body.removeEventListener('click', el.clickOutsideEvent);
      }
    }
  },
  methods: {
    toggleSelected (e) {
      e.target.classList.toggle('selected');
    },
    hideSelected (e) {
      if (!e.target.classList.contains('popup-container')) {
        Array.from(document.querySelectorAll('.selected')).forEach((el) => el.classList.remove('selected'));
      }
      if (e.target.classList.contains('filter-box')) {
        this.toggleSelected(e);
      }
    },
    closeFilters() {
      const filterArrays = [
        { filters: this.categoryFilter, type: 'categoryFilter' },
        { filters: this.difficultyFilter, type: 'difficultyFilter'  },
        { filters: this.ageFilter, type: 'ageFilter'  },
        { filters: this.formatFilter, type: 'formatFilter'  },
        { filters: this.trainingFilter, type: 'trainingFilter' },
        { filters: this.improPrepFilter, type: 'improPrepFilter' },
        { filters: this.keywordFilter, type: 'keywordFilter'  }   
      ]

      filterArrays.forEach((arr) => {
        this.$store.state.motions.filters[arr.type] = {}
        this.$store.state.motions.filters[arr.type] = arr.filters
      })
      this.$store.state.motions.filterCount += 1
      this.$emit('toggle-filters');
    },
    toggleFilters(event) {
      const popup = document.getElementById(event.target.getAttribute('data-type'));
      this.$store.state.motions.filters[event.target.getAttribute('data-type')] = {} // clean filter if we have bad state
      this.$store.state.motions.filters[event.target.getAttribute('data-type')] = this[event.target.getAttribute('data-type')]
      this.$store.state.motions.filterCount += 1
      popup.parentElement.classList.toggle('selected');
    },
    clearKeywords(event){
      this.keywordFilter = ''
    },
    randomMotion() {
      if(this.motion_length > 0) this.$router.push('/motion/' + (Math.floor((Math.random() * this.motion_length))+1))
    },
    chosenFiltersText (array) {
      if (array.length === 1) {
        return array[0].value;
      } else {
        return `${array[0].value} + ${array.length - 1} more`;
      }
    }
  },
  async created() {
    this.categoryArray = await this.$store.dispatch('getMotionAttributes', {type: 'categories'})
    this.difficultiesArray = await this.$store.dispatch('getMotionAttributes', {type: 'difficulties'})
    this.ageArray = await this.$store.dispatch('getMotionAttributes', {type: 'age-ranges'})
    this.formatArray = await this.$store.dispatch('getMotionAttributes', {type: 'debate-formats'})
    this.typeArray = await this.$store.dispatch('getMotionAttributes', {type: 'types'})
    this.improPrepArray = await this.$store.dispatch('getMotionAttributes', {type: 'impro-prep'})
    this.trainingFocusArray = await this.$store.dispatch('getMotionAttributes', {type: 'training-focuses'})
    this.motion_length = await this.$store.dispatch('getMotionLength')
  }
}
</script>

<style scoped lang="scss">


.search {
  font-size: 20px;
  margin: 0;
  color: #252525;
  font-family: "Poppins";
  width: 90%;
  @media (min-width: 768px) {
    font-size: 30px;
  }

    @media (min-width: 1400px) {
    width: 90%;
    margin: 0 auto;
  }

  @media (min-width: 1600px) {
    width: 80%;
  }

}
.filters-container {
  margin: 40px auto;
  width: 100%;
  display: grid;
  position: relative;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  column-gap: 3%;
  row-gap: 3%;

  @media (min-width: 1400px) {
    width: 90%;
    column-gap: 5%;
    row-gap: 5%;
    margin: 80px auto;
  }

  @media (min-width: 1600px) {
    width: 80%;
  }

  .filter-box {
    background-color: white;
    cursor: pointer;
    border: 4px solid white;
    height: 120px;

    @media (min-width: 576px) {
      position: relative;
      height: initial;
    }

    &:after {
      content: "";
      display: block;
      padding-bottom: 25%;

      @media (min-width: 576px) {
        padding-bottom: 90%;
        position: relative;
      }
    }

    &.selected {
      border: 4px solid #3098f3;

      /* Toggle this class when clicking on the popup container (hide and show the popup) */
      .popup-container {
        opacity: 1;
        z-index: 2;
        transition: z-index 0s;

        .popup-box label.popup-text {
          cursor: pointer;
        }
      }
    }

    .content {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;

      @media (min-width: 576px) {
        position: absolute;
      }

      img {
        width: 50%;
        pointer-events: none;

        @media (min-width: 1400px) {
          width: 40%;
        }
      }

      span {
        color: #252525;
        font-family: "IBM Plex Mono";
        font-size: 14px;
        line-height: 20px;
        text-align: center;
        padding: 10px;
        pointer-events: none;

        @media (min-width: 576px) {
          font-size: 18px;
        }
      }
    }

    &.filters-selected {
      background-color: #d6eafd;
      border-color: #d6eafd;

      &.selected {
        border-color: #3098f3;
      }

      img {
        width: 25%;
      }
    }

    .popup-container {
      opacity: 0;
      z-index: -1;
      transition: opacity 0.2s, z-index .1s 0.2s;
      background-color: white;
      color: black;
      border: 4px solid #3098f3;
      position: absolute;
      box-shadow: 0 0 27px 3px rgba(48, 152, 243, 0.5);
      cursor: default;

      &#keywordFilter {
        min-width: 300px;
      }

      .popup-box {
        padding: 20px;
        max-height: 300px;
        overflow-y: auto;

        .keyword-container {
          input {
            height: auto !important;
            border: 1px solid black;
            margin: 10px 0;
            width: 100%;

            @media (min-width: 576px) {
              width: 100%;
            }
          }
        }

        .keyword-apply {
          display: flex;
          justify-content: space-between;
          align-items: center;
          span {
            text-decoration: underline;
          }
        }

        .keyword-text {
          font-family: "IBM Plex Mono";
          font-size: 14px;
        }

        .checkmark-container {
          display: grid;
          grid-template-columns: 100%;
          column-gap: 20px;
          row-gap: 10px;
          width: 100%;
          align-items: start;
          border-bottom: 1px solid black;
          padding-bottom: 15px;

          @media (min-width: 992px) {
            grid-template-columns: 45% 45%;
          }
        }

        label.popup-text {
          cursor: default;
        }

        .popup-apply {
          color: #3098f3 !important;
          font-family: Poppins;
          font-size: 18px;
          font-weight: 700;
          text-align: right;
          text-decoration: underline;
        }
      }

      .popup-arrow {
        content: "";
        width: 20px;
        height: 20px;
        background: #fff;
        position: absolute;
        z-index: 1;
        border-left: 4px solid #3098f3;
        border-bottom: 4px solid #3098f3;
        left: 20px;
      }
    }

    &.bottom-popup {
      .popup-container {
        left: 0;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        @media (min-width: 576px) {
          left: -4px;
          right: initial;
          top: calc(100% + 28px);
          transform: none;
        }
      }

      .popup-arrow {
        transform: rotate(135deg);
        top: -14px;
        display: none;
        @media (min-width: 576px) {
          display: block;
        }
      }
    }

    &.top-popup {
      .popup-container {
        left: 0;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        @media (min-width: 576px) {
          left: -4px;
          right: initial;
          top: initial;
          bottom: calc(100% + 28px);
          transform: none;
        }
      }

      .popup-arrow {
        bottom: -14px;
        transform: rotate(-45deg);
        display: none;
        @media (min-width: 576px) {
          display: block;
        }
      }
    }
  }
  .filter-box:hover {
    background-color: #D6EAFD;
    border:#3098f3;
  }
  .randomFilterBox {
    background-color: transparent;
    border: 4px solid white;

    img {
      max-width: 30%;
    }

    span {
      font-size: 16px;
    }
  }
    .randomFilterBox:hover {
    background-color: transparent;
    border: 4px solid #ffcc00;
  }
}

.apply-button {
  display: flex;
  justify-content: center;

  .btn {
    margin-top: 20px;
    font-size: 14px;
    letter-spacing: 1px;
    padding: 5px 12px;
  }

  @media (min-width: 992px) {
    display: none;
  }
}

/* the actual input checkbox */
[type="checkbox"]:not(:checked),
[type="checkbox"]:checked {
  position: absolute;
  opacity: 0;
}

/* checkbox style for filters */
[type="checkbox"]:not(:checked) + label,
[type="checkbox"]:checked + label {
  position: relative;
  padding-left: 2.3em;
  font-size: 14px;
  line-height: 1.7;
  cursor: pointer;
  color: #000000;
  font-family: "IBM Plex Mono";
  font-style: italic;
  display: flex;
}

/* checkbox aspect */
[type="checkbox"]:not(:checked) + label:before,
[type="checkbox"]:checked + label:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 1.4em;
  height: 1.4em;
  border: 1px solid rgb(0, 0, 0);
  background: #FFF;
}

[type="checkbox"]:checked + label:before {
  background-image: url("../assets/checkbox.png");
  background-size: contain;
}

/* Accessibility */
[type="checkbox"]:checked:focus + label:before,
[type="checkbox"]:not(:checked):focus + label:before {
}

</style>
