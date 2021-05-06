<template>
  <div>
    <div class="filters-container">
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/topic.svg">
        <span :onclick="togglePopup"><i>Topic</i></span>
        <div class="popup">
          <div class="popup-container" id="myPopup">
            <div class="popup-box">
              <div class="checkmark-container">
                <div v-for="category in categories" :key="category">
                  <input :id="category" type='checkbox'/>
                  <label class="popup-text" :for="category">{{category}}</label>
                </div>
              </div>
              <div class="popup-apply">Apply</div>
            </div>
            <div class="popup-arrow">
            </div>
          </div>
        </div>
      </div>
      <div class="filterBox">
        <img src="../assets/difficulty.svg">
        <span><i>Difficulty</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/format.svg">
        <span><i>Format</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/age.svg">
        <span><i>Age</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/type.svg">
        <span><i>Motion type</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/focus.svg">
        <span><i>Training  focus</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/impro.svg">
        <span><i>Either impro or prep</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/keyword.svg">
        <span><i>Keyword</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/random.svg">
        <span><i>Show me a random motion</i></span>
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
        categories: [
          'Art and Culture',
          'Criminal Justice System',
          'Business',
          'Development',
        ]
      }
    },
    methods: {
      togglePopup: (event) => {
        var popup = document.getElementById("myPopup");
        popup.classList.toggle("show");
      },
      toggleFilters() {
        this.$emit('toggle-filters')
      }
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
  margin: 80px 0px 40px 0px;
  display: grid;
  grid-template-columns: 45% 45%;
  column-gap: 10%;
  row-gap: 5%;
  width: 100%;
  align-items: start;
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

  @media (min-width: 768px) {
    padding: 40px 10px;
  }

  img {
    max-width: 60%;
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

 /* Popup container */
.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
  width: 500px;
  max-width: 1000px !important;
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
  color: #3098f3;
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
  text-align: center;
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
