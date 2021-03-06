import React, { useState } from 'react';
import { useForm, SubmitHandler, Controller } from 'react-hook-form';
import ReactDatePicker from 'react-datepicker';
import { ErrorMessage } from '@hookform/error-message';
import { AddTransactionReq } from '../../api/requests';
import { AddTransactionBody } from '../../api/interfaces';
import { Transaction } from '../../interfaces';
import * as F from '../styled/Form';
import * as E from './constants';
import { AxiosError } from 'axios';
import 'react-datepicker/dist/react-datepicker.css';
import { mapAddTransaction } from '../../api/mappers';
import styled from 'styled-components';

interface FormMessage {
  type: 'error' | 'success' | 'empty';
  msg?: string;
}

const AddTransactionForm = () => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm<Transaction>({ criteriaMode: 'all' });

  const [formMsg, setFormMsg] = useState<FormMessage>();

  const clearErrors = () => {
    setFormMsg({ type: 'empty' });
  };

  const onSubmit: SubmitHandler<Transaction> = async (data) => {
    clearErrors();
    const dataBody = mapAddTransaction(data);
    await AddTransactionReq(dataBody)
      .then(() => {
        setFormMsg({ type: 'success', msg: E.LOGIN_SUCCESSFUL });
      })
      .catch((err: AxiosError) => {
        switch (err?.response?.status) {
          case 401:
            setFormMsg({ type: 'error', msg: E.WRONG_LOGIN_OR_PASSWORD });
            return;
          default:
            setFormMsg({ type: 'error', msg: E.UNSPECIFIC_REQUEST_ERROR });
            return;
        }
      });
  };

  return (
    <F.Container>
      <F.HeaderContainer>
        <F.Header>New transaction</F.Header>
      </F.HeaderContainer>
      <F.Form onSubmit={handleSubmit(onSubmit)}>
        <F.FormLabel htmlFor="date">
          <Controller
            control={control}
            name="date"
            render={({ field: { onChange, value } }) => (
              <ReactDatePicker
                onChange={onChange}
                selected={value}
                placeholderText="Select date"
              />
            )}
          />
          <span className="field-text">Transaction date</span>
          <ErrorMessage
            errors={errors}
            name="date"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="record-type">
          <select
            id="record-type"
            className="dropdown"
            {...register('record_type', { required: E.REQUIRED })}
          >
            <option selected disabled hidden>
              Record type
            </option>
            <option value="BUY">Buy</option>
            <option value="SELL">Sell</option>
          </select>
          <ErrorMessage
            errors={errors}
            name="record-type"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="symbol">
          <input
            id="symbol"
            placeholder="Symbol"
            {...register('symbol', { required: E.REQUIRED })}
          />
          <span className="field-text">Symbol</span>
          <ErrorMessage
            errors={errors}
            name="symbol"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="amount">
          <input
            id="amount"
            placeholder="Amount"
            {...register('amount', { required: E.REQUIRED, min: 0.000000001 })}
          />
          <span className="field-text">Amount</span>
          <ErrorMessage
            errors={errors}
            name="amount"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="fee">
          <input
            id="fee"
            type="number"
            placeholder="Fee"
            step="any"
            {...register('fee', { required: E.REQUIRED, min: 0.00, value: 0 })}
          />
          <span className="field-text">Fee</span>
          <ErrorMessage
            errors={errors}
            name="fee"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="price-per-unit">
          <input
            id="price-per-unit"
            type="number"
            placeholder="PricePerUnit"
            step="any"
            {...register('price_per_unit', { required: E.REQUIRED })}
          />
          <span className="field-text">Price per unit ($)</span>
          <ErrorMessage
            errors={errors}
            name="price-per-unit"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.Buttons>
          <F.ButtonContainer>
            <F.ButtonText className={`submit-${formMsg?.type}`}>
              {formMsg?.msg}
            </F.ButtonText>
            <F.SubmitButton
              type="submit"
              value="Add transaction"
            ></F.SubmitButton>
          </F.ButtonContainer>
        </F.Buttons>
      </F.Form>
    </F.Container>
  );
};

export default AddTransactionForm;
