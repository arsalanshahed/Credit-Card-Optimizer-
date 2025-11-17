'use client';

import { Sparkles, DollarSign } from 'lucide-react';
import MerchantLookup from './MerchantLookup';

interface CardRecommenderProps {
  merchant: string;
  amount: number;
  onMerchantChange: (value: string) => void;
  onAmountChange: (value: number) => void;
  onRecommend: () => void;
  isLoading: boolean;
}

export default function CardRecommender({
  merchant,
  amount,
  onMerchantChange,
  onAmountChange,
  onRecommend,
  isLoading,
}: CardRecommenderProps) {
  return (
    <div className="card max-w-2xl mx-auto mb-8">
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-semibold text-text mb-2">
            Merchant Name
          </label>
          <MerchantLookup
            value={merchant}
            onChange={onMerchantChange}
          />
        </div>

        <div>
          <label className="block text-sm font-semibold text-text mb-2">
            Purchase Amount ($)
          </label>
          <div className="relative">
            <DollarSign className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-text-light" />
            <input
              type="number"
              value={amount}
              onChange={(e) => onAmountChange(parseFloat(e.target.value) || 0)}
              min="0.01"
              step="0.01"
              className="input-field pl-12"
              placeholder="50.00"
            />
          </div>
        </div>

        <button
          onClick={onRecommend}
          disabled={isLoading}
          className="btn-primary w-full flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          {isLoading ? (
            <>
              <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              <span>Analyzing...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5" />
              <span>Optimize Rewards</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}

