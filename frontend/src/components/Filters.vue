<template>
  <div>
    <div class="filters-container">
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/topic.svg">
        <span :onclick="togglePopup" data-type="categoryFilter"><i>Category</i></span>
        <div class="popup">
          <div class="popup-container" id="categoryFilter">
            <div class="popup-box">
              <div class="checkmark-container">
                <div v-for="category in categoryArray" :key="category" >
                  <input :id="'category-' + category.id" type='checkbox' :value="{id: category.id, value: category.value}" v-model="categoryFilter"/>
                  <label class="popup-text" :for="'category-' + category.id">{{category.value}}</label>
                </div>
              </div>
              <div class="popup-apply" :onclick="toggleFilters"  data-type="categoryFilter">Apply</div>
            </div>
            <div class="popup-arrow">
            </div>
          </div>
        </div>
      </div>
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/difficulty.svg">
        <span :onclick="togglePopup" data-type="difficultyFilter"><i>Difficulty</i></span>
        <div class="popup">
          <div class="popup-container" id="difficultyFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/format.svg">
        <span :onclick="togglePopup" data-type="formatFilter"><i>Format</i></span>
        <div class="popup">
          <div class="popup-container" id="formatFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/age.svg">
        <span :onclick="togglePopup" data-type="ageFilter"><i>Age</i></span>
        <div class="popup">
          <div class="popup-container" id="ageFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/type.svg">
        <span :onclick="togglePopup" data-type="typeFilter"><i>Motion type</i></span>
        <div class="popup">
          <div class="popup-container" id="typeFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/focus.svg">
        <span :onclick="togglePopup" data-training="trainingFilter"><i>Training focus</i></span>
        <div class="popup">
          <div class="popup-container" id="trainingFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/impro.svg">
        <span :onclick="togglePopup" data-type="improPrepFilter"><i>Either impro or prep</i></span>
        <div class="popup">
          <div class="popup-container" id="improPrepFilter">
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
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/keyword.svg">
        <span :onclick="togglePopup" data-type="keywordFilter"><i>Keyword</i></span>
        <div class="popup">
          <div class="popup-container" id="keywordFilter">
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
      <div @click="randomMotion" :class="['filterBox', 'randomFilterBox']">
        <img src="../assets/random.svg">
        <span ><i>Show me a random motion</i></span>
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
    methods: {
      togglePopup: (event) => {
        const popup = document.getElementById(event.target.parentNode.attributes[0].value);
        popup.classList.toggle("show");
      },
      toggleFilters(event) {
        const popup = document.getElementById(event.target.getAttribute('data-type'));
        this.$store.state.motions.filters[event.target.getAttribute('data-type')] = {} // clean filter if we have bad state
        this.$store.state.motions.filters[event.target.getAttribute('data-type')] = this[event.target.getAttribute('data-type')]
        this.$store.state.motions.filterCount += 1
        popup.classList.toggle("show");
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
  margin: 40px 0;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  column-gap: 3%;
  row-gap: 3%;

  @media (min-width: 1200px) {
    column-gap: 5%;
    row-gap: 5%;
    margin: 80px 0 40px;
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

  @media (min-width: 768px) {
    display: none;
  }

}

/* Base for label styling */
[type="checkbox"]:not(:checked),
[type="checkbox"]:checked {
  position: absolute;
  left: 0;
  opacity: 0.01;
}
[type="checkbox"]:not(:checked) + label,
[type="checkbox"]:checked + label {
  position: relative;
  padding-left: 2.3em;
  font-size: 1.05em;
  line-height: 1.7;
  cursor: pointer;
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

/* Disabled checkbox */
[type="checkbox"]:disabled:not(:checked) + label:before,
[type="checkbox"]:disabled:checked + label:before {
  box-shadow: none;
  border-color: #bbb;
  background-color: #e9e9e9;
}

[type="checkbox"]:disabled:checked + label:after {
  color: #777;
}

[type="checkbox"]:disabled + label {
  color: rgb(199, 199, 199);
}

/* Accessibility */
[type="checkbox"]:checked:focus + label:before,
[type="checkbox"]:not(:checked):focus + label:before {
}

.checkmark-container {
  margin: 20px 0px 10px 0px;
  display: grid;
  grid-template-columns: 45% 45%;
  column-gap: 20px;
  row-gap: 10px;
  width: 100%;
  align-items: start;
}
.keyword-container {
  input {
    height: auto !important;
    border: 1px solid black;
    margin-top: 5px;
  } 
}
.selected {
  border: 4px solid #3098f3;
}

.filterBox {
  display: flex;
  flex-direction: column;
  background-color: white;
  align-items: center;
  padding: 20px 10px;
  cursor: 'pointer';

  @media (min-width: 768px) {
    padding: 40px 10px;
  }

  img {
    max-width: 60%;
  }
  &:hover {
    cursor: pointer;
  }
  span {
    color: #252525;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    line-height: 16px;
    text-align: center;
    margin-top: 10px;

    &:hover {
      cursor: pointer;
    }

    @media (min-width: 1400px) {
      margin-top: 15px;
      font-size: 24px;
      line-height: 26px;
    }
  }
}

.randomFilterBox {
  background-color: transparent;
  border: 4px solid white;

  img {
    max-width: 30%;
  }
}

 /* Popup container */
.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
}
.popup-text {
/* Style for "Nature Eco" */
  color: #000000;
  font-family: "IBM Plex Mono";
  font-size: 14px;
  font-style: italic;
  letter-spacing: normal;
  line-height: 47px;
  text-align: left;
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
  transform: rotate(-45deg);
  background: #fff;
  position: absolute;
  z-index: 1;
  border-left: 4px solid #3098f3;
  border-bottom: 4px solid #3098f3;
  margin-left: 20px;
  margin-top: -1px;
}


/* The actual popup (appears on top) */
.popup .popup-container {
  visibility: hidden;
  background-color: white;
  color: black;
  border: 4px solid #3098f3;
  padding: 8px 0;
  position: absolute;
  z-index: 2;
  bottom: 300%;
  left: 50%;
  margin-left: -80px;
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
.popup .show {
  visibility: visible;
  -webkit-animation: fadeIn 1s;
  animation: fadeIn 1s
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity:1 ;}
}

</style>
