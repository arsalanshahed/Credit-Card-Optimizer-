'use client';

import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';
import type { CardRecommendation } from '@/lib/types';
import { formatCurrency } from '@/lib/formatting';
import { DollarSign } from 'lucide-react';

interface SavingsSimulationChartProps {
  recommendations: CardRecommendation[];
}

export default function SavingsSimulationChart({
  recommendations,
}: SavingsSimulationChartProps) {
  const chartData = recommendations.map((card) => ({
    name: card.card_name.split(' ')[0], // Short name for display
    monthly: card.estimated_monthly_rewards,
    annual: card.estimated_annual_rewards,
    netAnnual: card.estimated_annual_rewards - card.annual_fee,
  }));

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-background/95 backdrop-blur-md border border-purple-500/30 rounded-lg p-3 shadow-xl">
          <p className="font-semibold text-purple-300 mb-2">{payload[0].payload.name}</p>
          {payload.map((entry: any, index: number) => (
            <p key={index} className="text-sm" style={{ color: entry.color }}>
              {entry.name}: {formatCurrency(entry.value)}
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay: 0.3 }}
    >
      <Card className="glass border-purple-500/20 shadow-xl">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <DollarSign className="w-5 h-5 text-purple-400" />
            Savings Simulation
          </CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#4a5568" />
              <XAxis
                dataKey="name"
                stroke="#a78bfa"
                tick={{ fill: '#a78bfa' }}
              />
              <YAxis
                stroke="#a78bfa"
                tick={{ fill: '#a78bfa' }}
                tickFormatter={(value) => `$${value}`}
              />
              <Tooltip content={<CustomTooltip />} />
              <Legend />
              <Bar
                dataKey="monthly"
                fill="#9333ea"
                name="Monthly Rewards"
                radius={[8, 8, 0, 0]}
              />
              <Bar
                dataKey="annual"
                fill="#ec4899"
                name="Annual Rewards"
                radius={[8, 8, 0, 0]}
              />
              <Bar
                dataKey="netAnnual"
                fill="#10b981"
                name="Net Annual (After Fee)"
                radius={[8, 8, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </motion.div>
  );
}


