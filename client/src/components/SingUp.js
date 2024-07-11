import React, {useState, useEffect} from 'react'
import {useFormik} from "formik"

function SingUp() {

    useEffect(() => {
        consoe.log("fetching data!")
        fetch("http://127.0.0.1:5000/signup")
        .then(res => res.json())
        .then((data) => {
        console.log(data)
        })
    })
  return (
    <div>
      
    </div>
  )
}

export default SingUp