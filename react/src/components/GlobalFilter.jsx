import React from 'react'
// import {Input} from "react-bootstrap";

export const GlobalFilter = ({ filter, setFilter }) => {
  return (
    <span>
      <Input 
        bsSize="sm"
        placeholder="Buscar" type='search' 
        filter={filter || ''}
        onChange={e => {
          setFilter(e.target.value)
        }}
      />
    </span>
  )
}