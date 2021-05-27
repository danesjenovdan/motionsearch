<template>
  <div>
    <div class="filters-container">
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/topic.svg">
          <span data-type="categoryFilter"><i>Category</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/difficulty.svg">
          <span data-type="difficultyFilter"><i>Difficulty</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/format.svg">
          <span data-type="formatFilter"><i>Format</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/age.svg">
          <span data-type="ageFilter"><i>Age</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/type.svg">
          <span data-type="typeFilter"><i>Motion type</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box bottom-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/focus.svg">
          <span data-training="trainingFilter"><i>Training focus</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box top-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/impro.svg">
          <span data-type="improPrepFilter"><i>Either impro or prep</i></span>
        </div>
        <div class="popup">
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
      </div>
      <div class="filter-box top-popup" @click="toggleSelected" v-outside="hideSelected">
        <div class="content">
          <img src="../assets/keyword.svg">
          <span data-type="keywordFilter"><i>Keyword</i></span>
        </div>
        <div class="popup">
          <div class="popup-container" id="keywordFilter" @click.stop>
            <div class="popup-box">
              <span class="keyword-text"> Enter key words, separated by comma.</span>
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
      </div>
      <div @click="randomMotion" :class="['filter-box', 'randomFilterBox']">
        <div class="content">
          <img src="../assets/random.svg">
          <span ><i>Show me a random motion</i></span>
        </div>
      </div>
    </div>
    <div class="apply-button">
      <button class="btn" @click="toggleFilters">Apply</button>
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
      improPrepArray: [{id: 0, value: 'impro'}, { id: 1, value: 'prep' }], // we don't have it saved in database
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
    toggleFilters(event) {
      const popup = document.getElementById(event.target.getAttribute('data-type'));
      this.$store.state.motions.filters[event.target.getAttribute('data-type')] = {} // clean filter if we have bad state
      this.$store.state.motions.filters[event.target.getAttribute('data-type')] = this[event.target.getAttribute('data-type')]
      this.$store.state.motions.filterCount += 1
      popup.parentElement.parentElement.classList.toggle('selected');
    },
    clearKeywords(event){
      this.keywordFilter = ''
    },
    randomMotion() {
      window.location.href = '/motion/' + (Math.floor((Math.random() * this.motion_length))+1);
    }
  },
  async created() {
    this.categoryArray = await this.$store.dispatch('getMotionAttributes', {type: 'categories'})
    this.difficultiesArray = await this.$store.dispatch('getMotionAttributes', {type: 'difficulties'})
    this.ageArray = await this.$store.dispatch('getMotionAttributes', {type: 'age-ranges'})
    this.formatArray = await this.$store.dispatch('getMotionAttributes', {type: 'debate-formats'})
    this.typeArray = await this.$store.dispatch('getMotionAttributes', {type: 'types'})
    this.trainingFocusArray = await this.$store.dispatch('getMotionAttributes', {type: 'training-focuses'})
    this.motion_length = await this.$store.dispatch('getMotionLength')
  }
}
</script>

<style scoped lang="scss">

.filters-container {
  margin: 40px auto;
  width: 100%;
  display: grid;
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
    position: relative;
    display: flex;
    //align-items: center;

    &:after {
      content: "";
      display: block;
      padding-bottom: 90%;
    }

    .content {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;
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
      font-size: 18px;
      line-height: 20px;
      text-align: center;
      padding: 10px;
      pointer-events: none;
    }

    &.selected {
      border: 4px solid #3098f3;
    }
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
  -webkit-transition: all .275s;
      transition: all .275s;
}
  [type="checkbox"]:checked + label:before {
    background: #3098f3;
  }

/* checked mark aspect */
[type="checkbox"]:not(:checked) + label:after,
[type="checkbox"]:checked + label:after {
  content: '✓';
  position: absolute;
  top: .525em;
  left: .18em;
  font-size: 1.375em;
  color: #ffffff;
  line-height: 0;
  -webkit-transition: all .2s;
      transition: all .2s;
}

/* checked mark aspect changes */
[type="checkbox"]:not(:checked) + label:after {
  opacity: 0;
  -webkit-transform: scale(0) rotate(45deg);
      transform: scale(0) rotate(45deg);
}

[type="checkbox"]:checked + label:after {
  opacity: 1;
  -webkit-transform: scale(1) rotate(0);
      transform: scale(1) rotate(0);
}

/* Accessibility */
[type="checkbox"]:checked:focus + label:before,
[type="checkbox"]:not(:checked):focus + label:before {
}

.checkmark-container {
  margin: 20px 0px 10px 0px;
  display: grid;
  grid-template-columns: 100%;
  column-gap: 20px;
  row-gap: 10px;
  width: 100%;
  align-items: start;

  @media (min-width: 992px) {
    grid-template-columns: 45% 45%;
  }
}
.keyword-container {
  input {
    height: auto !important;
    border: 1px solid black;
    margin-top: 5px;
  }
}

 /* Popup container */
.popup {
  position: relative;
}

.popup-apply {
  color: #3098f3 !important;
  font-family: Poppins;
  font-size: 18px;
  font-weight: 700;
  font-style: normal;
  letter-spacing: normal;
  line-height: 47px;
  text-align: right;
  text-decoration: underline;
  border-top: 1px solid black;
}
.keyword-apply {
  display: flex;
  justify-content: space-between;
  font-weight: 700;
  font-style: normal;
  letter-spacing: normal;
  line-height: 47px;
  text-align: right;
  border-top: 1px solid black;
  span {
    text-decoration: underline;
  }
}
.keyword-text {
  display: flex;
  justify-content: space-between;
  font-weight: 700;
  font-style: normal;
  letter-spacing: normal;
  line-height: 47px;
  text-align: right;
}
.popup-box {
  margin: 10px;
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

.filter-box.bottom-popup {
  flex-direction: column-reverse;

  .popup-container {
    top: 28px;
  }

  .popup-arrow {
    transform: rotate(135deg);
    top: -14px;
  }
}

.filter-box.top-popup {
  flex-direction: column;

  .popup-container {
    bottom: 28px;
  }

  .popup-arrow {
    transform: rotate(-45deg);
  }
}

/* The actual popup (appears on top) */
.popup .popup-container {
  opacity: 0;
  transition: opacity 0.2s;
  background-color: white;
  color: black;
  border: 4px solid #3098f3;
  padding: 8px;
  position: absolute;
  left: -4px;
  z-index: -1;
  box-shadow: 0 0 27px 3px rgba(48, 152, 243, 0.5);
}

/* Popup arrow */
.popup .popuptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  z-index: -1;
  border-color: #555 transparent transparent transparent;
}

/* Toggle this class when clicking on the popup container (hide and show the popup) */
.selected .popup .popup-container {
  opacity: 1;
  z-index: 2;
}

</style>
