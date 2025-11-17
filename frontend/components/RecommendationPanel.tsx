'use client';

import { motion } from 'framer-motion';
import type { RecommendationResponse } from '@/lib/api-client';
import CardResult from './CardResult';
import RewardChart from './RewardChart';
import CardList from './CardList';

interface RecommendationPanelProps {
  result: RecommendationResponse;
}

export default function RecommendationPanel({ result }: RecommendationPanelProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="space-y-8"
    >
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <CardResult result={result} />
        <RewardChart result={result} />
      </div>
      <CardList result={result} />
    </motion.div>
  );
}

