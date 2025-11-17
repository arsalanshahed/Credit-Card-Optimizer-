'use client';

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { formatCurrency } from '@/lib/formatting';

interface SpendingChartProps {
  data: Array<{ category: string; amount: number }>;
}

export default function SpendingChart({ data }: SpendingChartProps) {
  return (
    <div className="card">
      <h3 className="text-lg font-heading font-semibold mb-4 text-text">
        Spending by Category
      </h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
          <XAxis
            dataKey="category"
            tick={{ fill: '#64748B', fontSize: 12 }}
          />
          <YAxis
            tick={{ fill: '#64748B', fontSize: 12 }}
            tickFormatter={(value) => `$${value}`}
          />
          <Tooltip
            formatter={(value: number) => formatCurrency(value)}
          />
          <Bar dataKey="amount" fill="#4F46E5" radius={[8, 8, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

