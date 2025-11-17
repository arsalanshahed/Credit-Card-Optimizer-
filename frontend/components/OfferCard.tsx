'use client';

import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import type { CardRecommendation } from '@/lib/types';
import { formatCurrency, formatPercentage } from '@/lib/formatting';
import { Award, CreditCard, TrendingUp, CheckCircle2 } from 'lucide-react';

interface OfferCardProps {
  recommendation: CardRecommendation;
  isBest?: boolean;
  index: number;
}

export default function OfferCard({
  recommendation,
  isBest = false,
  index,
}: OfferCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 50, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{
        delay: index * 0.1,
        type: 'spring',
        stiffness: 100,
      }}
      whileHover={{ scale: 1.02, y: -5 }}
      className="h-full"
    >
      <Card
        className={`glass border-purple-500/20 shadow-xl h-full transition-all ${
          isBest
            ? 'border-purple-500/50 bg-gradient-to-br from-purple-900/20 to-pink-900/20'
            : 'hover:border-purple-500/40'
        }`}
      >
        <CardHeader>
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <CardTitle className="flex items-center gap-2 mb-2">
                <CreditCard className="w-5 h-5 text-purple-400" />
                {recommendation.card_name}
                {isBest && (
                  <Badge className="bg-gradient-to-r from-yellow-500 to-orange-500">
                    <Award className="w-3 h-3 mr-1" />
                    Best Choice
                  </Badge>
                )}
              </CardTitle>
              <p className="text-sm text-muted-foreground">{recommendation.issuer}</p>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between p-3 bg-purple-500/10 rounded-lg">
            <span className="text-sm text-muted-foreground">Reward Rate</span>
            <span className="text-2xl font-bold text-purple-400">
              {formatPercentage(recommendation.reward_rate)}
            </span>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div className="p-3 bg-background/50 rounded-lg">
              <p className="text-xs text-muted-foreground mb-1">Monthly</p>
              <p className="text-lg font-semibold text-green-400">
                {formatCurrency(recommendation.estimated_monthly_rewards)}
              </p>
            </div>
            <div className="p-3 bg-background/50 rounded-lg">
              <p className="text-xs text-muted-foreground mb-1">Annual</p>
              <p className="text-lg font-semibold text-green-400">
                {formatCurrency(recommendation.estimated_annual_rewards)}
              </p>
            </div>
          </div>

          <div className="flex items-center justify-between pt-2 border-t border-purple-500/20">
            <span className="text-sm text-muted-foreground">Annual Fee</span>
            <span
              className={`font-semibold ${
                recommendation.annual_fee > 0 ? 'text-red-400' : 'text-green-400'
              }`}
            >
              {recommendation.annual_fee > 0
                ? formatCurrency(recommendation.annual_fee)
                : 'Free'}
            </span>
          </div>

          {recommendation.cashback_breakdown.length > 0 && (
            <div className="pt-2 border-t border-purple-500/20">
              <p className="text-xs text-muted-foreground mb-2">Category Breakdown</p>
              <div className="space-y-1">
                {recommendation.cashback_breakdown.slice(0, 3).map((item, idx) => (
                  <div key={idx} className="flex items-center justify-between text-xs">
                    <span className="text-muted-foreground">{item.category}</span>
                    <div className="flex items-center gap-2">
                      <span className="text-purple-400">{formatPercentage(item.rate)}</span>
                      <span className="text-green-400">{formatCurrency(item.amount)}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </motion.div>
  );
}


