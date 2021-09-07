
/* eslint-disable */
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let blog = '정부 소외 계층을 위한 웹 프로그램';

  let [글제목, 글제목변경] = useState(['부분 텍스트 음성변환', '전체 텍스트 음성변환', '화면 확대', '색상 반전']);
  let [좋아요, 좋아요변경] = useState(0);

  function 제목바꾸기(){
    var newArray = [...글제목]; // deep copy, 값을 공유하지 않게 하기 위해 ...을 추가함
    newArray[0] = '여자코트 추천';
    글제목변경(newArray); 
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div>{blog}</div>
      </div>
      <div className="list">
        <h3> {글제목[0]}<span onClick={ () => {좋아요변경(좋아요+1)}}>👍</span> {좋아요} </h3>
        <p>2월 17일 발행</p>
        <button onClick={ 제목바꾸기 }>버튼</button>
        <hr/>
      </div>

      <div className="list">
        <h3>{글제목[1]}</h3>
        <p>2월 19일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3>{글제목[2]}</h3>
        <p>2월 21일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3>{글제목[3]}</h3>
        <p>2월 24일 발행</p>
        <hr/>
      </div>

      <Modal></Modal> 
      {/* component */}

    </div>
  );
}

function Modal(){
  return (
    <div>
    <h2>제목</h2>
    <p>날짜</p>
    <p>상세내용</p>
  </div>
  )
}

export default App;
