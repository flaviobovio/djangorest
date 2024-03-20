

import React, {useState, useEffect, useMemo, useCallback} from "react";
import { Container, Row, Col, Table, Button, ButtonGroup, Form} from "react-bootstrap";
// Input, InputGroup, InputGroupText, , Label
import Axios from "axios";
import { useTable, usePagination, useSortBy, useGlobalFilter} from 'react-table'


import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowUp} from '@fortawesome/free-solid-svg-icons'
import { faArrowDown} from '@fortawesome/free-solid-svg-icons'
import { GlobalFilter } from "../components/GlobalFilter";
import {} from "./SwimmerFormPage"



export function SwimmerPage() {

  // const [data, setData] = useState([]);

  // Using useEffect to call the API once mounted and set the data
  // useEffect(() => {
  //   (async () => {
  //     const result = await Axios("https://flavioboviovt.pythonanywhere.com/api/v1/swimmer/");
  //     setData(result.data);
  //   })();
  // }, []);

  //   const handleAgregar =  (e) => {
  //   const newdata = [...data, e];
  //   setData(newdata);
  // }

  const data = [
    {
        "id": 1,
        "name": "Flavio Bovio",
        "age": 51,
        "club": "Reus",
        "city": "Venado Tuerto",
        "created_at": "2024-03-12T23:47:17.475605Z",
        "updated_at": "2024-03-12T23:47:17.475654Z"
    },
    {
        "id": 2,
        "name": "Morero Mauro Alejandro",
        "age": 38,
        "club": "Reus",
        "city": "Venado Tuerto",
        "created_at": "2024-03-13T00:48:56.969798Z",
        "updated_at": "2024-03-13T22:46:51.349130Z"
    },
    {
        "id": 3,
        "name": "Cicerchia Daniel",
        "age": 48,
        "club": "Reus",
        "city": "Venado Tuerto",
        "created_at": "2024-03-15T15:42:24.842796Z",
        "updated_at": "2024-03-15T15:42:24.843145Z"
    }
]


  // // Uso useCallback para evitar warnings en useMemo Columns
  // const handleEditar = useCallback((e) => {
  //   const newdata = [...data];
  //   const i = newdata.findIndex(item => item.id === e.id);
  //   newdata[i] = e;
  //   setData(newdata);
  // }, [data]);

  // // Uso useCallback para evitar warnings en useMemo Columns
  // const handleBorrar = useCallback((id) => {
  //   const newdata = [...data].filter(i => i.id !== id);  
  //   setData(newdata);
  // }, [data]);

  const columns = useMemo(
    () => [
      {
        Header: 'ID',
        accessor: 'id', 
      },
      {
        Header: 'Name',
        accessor: 'name',
      },
      {
        Header: 'Age',
        accessor: 'age',
      },
      {
        Header: 'Club',
        accessor: 'club',
      },

    //   ,{Header: '',
    //   accessor: 'action',
    //   Cell: row => (
    //   <div>
    //     edit /delete
    //      <NadadorForm data={row.row.original} handleEditar={handleEditar} handleBorrar={handleBorrar}/>
    //   </div>
    //   )},
    ],
    // [handleEditar, handleBorrar]
  )

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
    page,
    nextPage,
    previousPage,
    canPreviousPage,
    canNextPage,
    pageOptions,
    state,
    gotoPage,
    pageCount,
    setPageSize,
    setGlobalFilter,
  } = useTable( 
    {
      columns,
      data,
      initialState: { pageIndex: 0 },
      autoResetGlobalFilter: false,
      autoResetPage: false,  
    },
    useGlobalFilter,
    useSortBy,
    usePagination, 
  )

  const { pageIndex, pageSize, globalFilter } = state  


  return (
    <Container 
      className="bg-light border"
      fluid
      style={{ marginTop: "20px" }}
    >

      <Row style={{ marginTop: "10px" }}>

      <Col align='left'>
        <h5>Nadadores</h5>
      </Col>
      {/* <Col align="right" onChange={() => gotoPage(0)}>
        <GlobalFilter filter={globalFilter} setFilter={setGlobalFilter}/>        
      </Col>         */}
      <Col align='left'>
        {/* <Label size="sm">{rows.length}/{data.length}</Label> */}
      </Col>
      <Col align="right">
        {/* <NadadorForm 
          data={{id: 0, sexo:'F'}} 
          handleAgregar = {handleAgregar}
        />          */}
      </Col>        
      </Row>

      <Row style={{marginTop: "10px", marginBottom: "10px" }} className="border-top"></Row>            

<Row>
  <Table size="sm" striped {...getTableProps()}>
    <thead>
      {headerGroups.map(headerGroup => (
        <tr {...headerGroup.getHeaderGroupProps()}>
          {headerGroup.headers.map(column => (
            <th
              {...column.getHeaderProps(column.getSortByToggleProps())}
            >
              {column.render('Header')}
              <span>{' '}
                {column.isSorted
                  ? column.isSortedDesc
                    ? <FontAwesomeIcon icon={faArrowDown} />
                    : <FontAwesomeIcon icon={faArrowUp} />
                  : ''}
              </span>                  
            </th>
          ))}
        </tr>
      ))}
    </thead>
    <tbody {...getTableBodyProps()}>
      {page.map(row => {
        prepareRow(row)
        return (
          <tr {...row.getRowProps()}>
            {row.cells.map(cell => {
              return (
                <td
                  {...cell.getCellProps()}
                >
                  {cell.render('Cell')}
                </td>
              )                 
            })}
          </tr>
        )
      })}
    </tbody>
  </Table>
</Row>
{/* <Row>
  <Col>
    <ButtonGroup>
      <Button className="me-2" size="sm" onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
        {'<<'}
      </Button>

      <Button className="me-2" size="sm" onClick={() => previousPage()} disabled={!canPreviousPage}>
          Anterior
      </Button>
      
      <Button className="me-2" size="sm" onClick={() => nextPage()} disabled={!canNextPage}>
        Siguiente
      </Button>

      <Button className="me-2" size="sm" onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
        {'>>'}
      </Button>

    </ButtonGroup>
  </Col>
  <Col>
    <InputGroup size="sm">
      <InputGroupText>Ir a Página</InputGroupText>
      <Input
        name="pagina"
        type='number'
        defaultValue={pageIndex + 1}
        onChange={e => {
          const pageNumber = e.target.value ? Number(e.target.value) - 1 : 0
          gotoPage(pageNumber)
        }}
      />
    </InputGroup>        
  </Col>

  <Col>
    <Input type="select"
        size="sm" 
        value={pageSize}
        onChange={e => setPageSize(Number(e.target.value))}>
        {[5, 10, 25, 50].map(pageSize => (
          <option key={pageSize} value={pageSize}>
            Mostrar {pageSize}
          </option>
        ))}
    </Input>      
  </Col>

  <Col>
    <InputGroup size="sm" align="right">
      <InputGroupText>Página</InputGroupText>
      <InputGroupText>{pageIndex + 1} de {pageOptions.length}</InputGroupText>
    </InputGroup>
  </Col>
</Row> */}









   </Container>
   )

}

