import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 650,
  },
}));


export default function TableDisplay(props) {
  const classes = useStyles();
  let rows = JSON.parse(props.processed_text);
  console.log(rows)
  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell>Book Names</TableCell>
            <TableCell align="left">Year of Pub</TableCell>
            <TableCell align="left">Author</TableCell>
            <TableCell align="left">Publisher</TableCell>
            <TableCell align="left">ISBN</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.name}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="left">{row.yop}</TableCell>
              <TableCell align="left">{row.author}</TableCell>

              <TableCell align="left">{row.publisher}</TableCell>
              <TableCell align="left">{row.isbn}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}