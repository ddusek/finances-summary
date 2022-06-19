import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import {
  COLOR_DARK,
  COLOR_COMPONENT_LIGHT,
  COLOR_COMPONENT_DARK,
  FONT_SIZE_BIG,
  COLOR_LIGHT_GREY,
  COLOR_MEDIUM_GREY,
  COLOR_DARK_GREY,
} from '../utils/cssConstants';
import { Transaction } from '../interfaces';
import { GetTransactions } from '../api/requests';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
  font-size: ${FONT_SIZE_BIG};
  margin: 30px;
  overflow: auto;
  
  ::-webkit-scrollbar {
    width: 10px;
  }
  ::-webkit-scrollbar-track {
    background: ${COLOR_DARK_GREY};
  }
  ::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: ${COLOR_LIGHT_GREY};
  }
  ::-webkit-scrollbar-thumb:hover {
    background: ${COLOR_MEDIUM_GREY};
  }
`;

const Table = styled.table`
  min-width: 1200px;
  border-spacing: 0px;
  width: 100%;
  background-color: ${COLOR_DARK};
  border-radius: 10px;
  tr:last-child td:first-child {
    border-bottom-left-radius: 10px;
  }

  tr:last-child td:last-child {
      border-bottom-right-radius: 10px;
  }
`;

const HeaderTr = styled.tr`
  width: 100%;
`

const HeaderItem = styled.th`
  min-width: 100px;
  height: 60px;
  padding: 0 15px;
`;

const TableTr = styled.tr`
  background: ${COLOR_COMPONENT_LIGHT};
  :nth-child(even) {
    background: ${COLOR_COMPONENT_DARK};
  }
`;

const Item = styled.td`
  min-width: 100px;
  height: 50px;
  text-align: center;
  padding: 0 15px;

  &.buy {
    color: #68ff68;
    font-weight: 600;
  }
  &.sell {
    color: #ff6565;
    font-weight: 600;
  }
  &.gain {
    color: #68ff68;
  }
  &.loss {
    color: #ff6565;
  }
`;

const TransactionsHistory = () => {
  const [transactions, setTransactions] = useState<Transaction[] | undefined>();

  useEffect(() => {
    const getTransactionsData = async () => {
      const response = await GetTransactions('?type=buy&symbol=btc');
      const data = response.data;
      setTransactions(data);
    };
    getTransactionsData();
  }, []);

  const getRecordTypeClass = (recordType: Transaction['record_type']) => {
    switch (recordType) {
      case 'BUY':
        return 'buy';
      case 'SELL':
        return 'sell';
      default:
        return '';
    }
  };

  const determineChangeColor = (change: number) => {
    if (change > 0) {
      return 'gain'
    } else if (change < 0) {
      return 'loss'
    }
    return ''
  }

  const formatChange = (change: number, type: 'PERCENT' | 'NUMBER') => {
    const sign = change > 0? '+': '';
    const unit = type === 'NUMBER'? '$': '%';
    return `${sign}${change}${unit}`;
  }

  return !transactions ? (
    <Container></Container>
  ) :
  (
    <Container>
      <Table>
        <thead>
          <HeaderTr>
            <HeaderItem>Date</HeaderItem>
            <HeaderItem>Type</HeaderItem>
            <HeaderItem>Symbol</HeaderItem>
            <HeaderItem>Amount</HeaderItem>
            <HeaderItem>Price per unit ($)</HeaderItem>
            <HeaderItem>Unrealized Change ($)</HeaderItem>
            <HeaderItem>Unrealized Change (%)</HeaderItem>
            <HeaderItem>Realized Change ($)</HeaderItem>
            <HeaderItem>Realized Change (%)</HeaderItem>
          </HeaderTr>
        </thead>
        <tbody>
          {transactions.map((t, i) => {
            return (
              <TableTr key={i}>
                <Item>{t.date}</Item>
                <Item className={getRecordTypeClass(t.record_type)}>
                  {t.record_type}
                </Item>
                <Item>{t.symbol}</Item>
                <Item>{t.amount}</Item>
                <Item>{t.price_per_unit}$</Item>
                <Item className={determineChangeColor(t.change_number_today)}>
                  {formatChange(t.change_number_today, 'NUMBER')}
                </Item>
                <Item className={determineChangeColor(t.change_percent_today)}>
                  {formatChange(t.change_percent_today, 'PERCENT')}
                </Item>
                <Item className={determineChangeColor(t.change_number_all_time)}>
                  {formatChange(t.change_number_all_time, 'NUMBER')}
                </Item>
                <Item className={determineChangeColor(t.change_percent_all_time)}>
                  {formatChange(t.change_percent_all_time, 'PERCENT')}
                </Item>
              </TableTr>
            );
          })}
        </tbody>
      </Table>
    </Container>
  );
};

export default TransactionsHistory;
