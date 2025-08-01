import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Paper, Grid } from '@mui/material';
import axios from 'axios';

function App() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState('');
  const [operation, setOperation] = useState('add');

  const calculate = async () => {
    try {
      const response = await axios.post('http://localhost:5000/calculate', {
        operation,
        num1,
        num2: operation !== 'square' && operation !== 'sqrt' ? num2 : null
      });
      setResult(response.data.result);
    } catch (error) {
      setResult(`Error: ${error.response?.data?.error || error.message}`);
    }
  };

  return (
    <Container maxWidth="sm">
      <Paper elevation={3} style={{ padding: '20px', marginTop: '20px' }}>
        <Typography variant="h4" align="center" gutterBottom>
          Base-Caltor
        </Typography>
        
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              fullWidth
              label="Number 1"
              variant="outlined"
              type="number"
              value={num1}
              onChange={(e) => setNum1(e.target.value)}
            />
          </Grid>
          
          {operation !== 'square' && operation !== 'sqrt' && (
            <Grid item xs={12}>
              <TextField
                fullWidth
                label="Number 2"
                variant="outlined"
                type="number"
                value={num2}
                onChange={(e) => setNum2(e.target.value)}
              />
            </Grid>
          )}
          
          <Grid item xs={12}>
            <select 
              value={operation} 
              onChange={(e) => setOperation(e.target.value)}
              style={{ width: '100%', padding: '10px', fontSize: '16px' }}
            >
              <option value="add">Add</option>
              <option value="subtract">Subtract</option>
              <option value="multiply">Multiply</option>
              <option value="divide">Divide</option>
              <option value="square">Square</option>
              <option value="sqrt">Square Root</option>
            </select>
          </Grid>
          
          <Grid item xs={12}>
            <Button 
              fullWidth 
              variant="contained" 
              color="primary" 
              onClick={calculate}
            >
              Calculate
            </Button>
          </Grid>
          
          {result && (
            <Grid item xs={12}>
              <Typography variant="h6" align="center">
                Result: {result}
              </Typography>
            </Grid>
          )}
        </Grid>
      </Paper>
    </Container>
  );
}

export default App;