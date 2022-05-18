import styled from 'styled-components';
import AddTransactionForm from '../components/forms/AddTransaction';
import TransactionsHistory from '../components/TransactionsHistory';

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(2, 50%);
  /* grid-template-rows: repeat(2, 600px); */
  grid-gap: 50px 0;
  margin: 20px;
`;

const GridItemOne = styled.div`
  grid-column: 1;
  grid-row: 1;
`;

const GridItemTwo = styled.div`
  grid-column: 2;
  grid-row: 1;
`;

const GridItemThree = styled.div`
  grid-column-start: 1;
  grid-column-end: 3;
`;

const GridItemFour = styled.div`
  grid-column: 1;
  grid-row: 3;
`;

const Home = () => {
  return (
    <Grid>
      <GridItemOne>
        <h2>Add new transaction</h2>
        <AddTransactionForm />
      </GridItemOne>
      <GridItemTwo>
        <h2>someying</h2>
        <AddTransactionForm />
      </GridItemTwo>
      <GridItemThree>
        <h2>Last transactions</h2>
      <TransactionsHistory />
      </GridItemThree>
      <GridItemFour>
        <h2>Something something</h2>
        <span>asdf</span>
      </GridItemFour>
    </Grid>
  );
};

export default Home;
